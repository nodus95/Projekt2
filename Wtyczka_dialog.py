# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Projekt2Dialog
                                 A QGIS plugin
 Wtyczka na projekt 2 z Informatyki Geodezyjnej
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-09
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Antoszkiewicz_Chudy
        email                : 01169821@pw.edu.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from qgis.core import QgsMessageLog
from qgis.core import QgsProject, Qgis, QgsPointXY
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Wtyczka_dialog_base.ui'))

class Projekt2Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Projekt2Dialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        # Add the comboBoxLayer attribute
        self.comboBoxLayer = self.maplayer_layer

        self.pushbutton_policz.clicked.connect(self.policz_wysokosc)

        # Select the first layer in the comboBoxLayer
        if self.comboBoxLayer.count() > 0:
            self.comboBoxLayer.setCurrentIndex(0)

    def policz_wysokosc(self):
        print("Starting policz_wysokosc")
        print(f"Current layer index: {self.maplayer_layer.currentIndex()}")
        print(f"Current layer data: {self.maplayer_layer.currentData()}")

        active_layer_name = self.comboBoxLayer.currentText()
        active_layer = QgsProject.instance().mapLayersByName(active_layer_name)

        if len(active_layer) == 0:
            QgsMessageLog.logMessage("Nie można uzyskać aktywnej warstwy.", level=Qgis.Warning)
            return

        active_layer = active_layer[0]

        selected_features = active_layer.selectedFeatures()

        if len(selected_features) < 2:
            QgsMessageLog.logMessage("Wybierz co najmniej 2 obiekty na warstwie.", level=Qgis.Warning)
            return

        if len(selected_features) == 2:
            feature_1 = selected_features[0]
            feature_2 = selected_features[1]

            punkt_1 = feature_1.attribute('nr_punktu')
            punkt_2 = feature_2.attribute('nr_punktu')

            if feature_1.attribute('h_plevrf2007nh'):
                roznica_wysokosci = round(float(feature_1.attribute('h_plevrf2007nh')) - float(feature_2.attribute('h_plevrf2007nh')), 4)
                system_wysokosci = 'PL_EVRF2007'
            elif feature_1.attribute('h_plkron86nh'):
                roznica_wysokosci = round(float(feature_1.attribute('h_plkron86nh')) - float(feature_2.attribute('h_plkron86nh')),4)
                system_wysokosci = 'PL_KRON86'
            else:
                QgsMessageLog.logMessage("Nieobsługiwany system wysokości.", level=Qgis.Warning)

            result_message = f"Różnica wysokości między punktami {punkt_1} i {punkt_2} w systemie wysokościowym {system_wysokosci} wynosi: {roznica_wysokosci} [m]"
            QgsMessageLog.logMessage(result_message, level=Qgis.Info)

        if len(selected_features) > 2:
            self.policz_pole(selected_features)

    def policz_pole(self, selected_features):
        print("Starting policz_pole")
        print(f"Current layer index: {self.maplayer_layer.currentIndex()}")
        print(f"Current layer data: {self.maplayer_layer.currentData()}")

        #Pobieranie współrzędnych zaznaczonych punktów
        punkty = []
        for feature in selected_features:
            x = float(feature.attribute('x2000'))
            y = float(feature.attribute('y2000'))
            point = QgsPointXY(x, y)
            punkty.append(point)

        #Pole powierzchni metodą Gaussa
        pole = 0.0
        ilosc_pkt = len(punkty)
        for i in range(ilosc_pkt):
            j = (i + 1) % ilosc_pkt
            pole += (punkty[j].x() + punkty[i].x()) * (punkty[j].y() - punkty[i].y())

        pole /= 2.0
        pole = abs(pole)

        #Pobieranie numerów punktów
        point_numbers = [feature.attribute('nr_punktu') for feature in selected_features]

        #Tworzenie wiadomości z wynikiem
        result_message = f"Pole powierzchni figury o wierzchołkach w punktach o numerach: {', '.join(point_numbers)} wynosi: {pole} [m²]"

        # Wyświetlenie wiadomości na pasku informacyjnym
        iface.messageBar().pushMessage("Obliczenie pola powierzchni", result_message, level=Qgis.Success)
