from dataclasses import dataclass
import os
import json
import typing

import streamlit.components.v1 as components
import streamlit as st
import pandas as pd

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "EJ2PivotGrid",
        url="http://localhost:3001",
    )

else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("EJ2PivotGrid", path=build_dir)


def SfPivotGrid(Data: pd.DataFrame = None, Props: typing.Dict = None):
    if Data is not None:
        dataSet = PdToJson(Data)

    elif Props.dataSource is not None:
        dataSet = PdToJson(Props.dataSource)

    if Props.dataSourceSettings.get("dataSource") is not None:
        Props.dataSourceSettings["dataSource"] = PdToJson(
            Props.dataSourceSettings["dataSource"]
        )

    if Props is None:
        Props = PivotGridProps(dataSet)

    if Data is not None or Props is not None:
        params = {
            "data": dataSet,
            "licenseKey": Props._PivotGridProps__license_key,
            "theme": Props.theme,
            "dataSourceSettings": Props.dataSourceSettings,
            "gridSettings": Props.gridSettings,
            "chartSettings": Props.chartSettings,
            "editSettings": Props.editSettings,
            "toolbar": Props.toolbar,
            "showToolbar": Props.showToolbar,
            "allowExcelExport": Props.allowExcelExport,
            "allowPdfExport": Props.allowPdfExport,
            "allowConditionalFormatting": Props.allowConditionalFormatting,
            "showGroupingBar": Props.showGroupingBar,
            "allowDeferLayoutUpdate": Props.allowDeferLayoutUpdate,
            "allowCalculatedField": Props.allowCalculatedField,
            "allowDrillThrough": Props.allowDrillThrough,
            "showFieldList": Props.showFieldList,
            "height": Props.height,
            "width": Props.width,
            "displayOption": Props.displayOption,
            "chartTypes": Props.chartTypes,
        }
        component_value = _component_func(params=params)
        return component_value
    else:
        st.warning("Provide data to render Pivot Grid component", icon="⚠️")


def PdToJson(dataframe: pd.DataFrame):
    json_obj = json.loads(dataframe.to_json())
    dict_keys = list(json_obj.keys())
    json_list = []

    for index in range(len(json_obj[dict_keys[0]])):
        row_obj = dict()
        for column in dict_keys:
            row_obj[column] = json_obj[column][str(index)]
        json_list.append(row_obj)

    return json_list


class PivotGridProps:

    def __init__(self, data: pd.DataFrame = None):
        self.dataSource = data
        self.allowExcelExport = False
        self.allowPdfExport = False
        self.allowConditionalFormatting = True
        self.showGroupingBar = False
        self.allowDeferLayoutUpdate = True
        self.allowCalculatedField = True
        self.allowDrillThrough = True
        self.showFieldList = True
        self.theme = "https://cdn.syncfusion.com/ej2/22.1.34/material.css"
        self.__license_key = None
        self.dataSourceSettings = {
            "dataSource": data,
            "columns": [],
            "values": [],
            "rows": [],
            "filters": [],
            "formatSettings": [],
            "calculatedFieldSettings": [],
            "conditionalFormatSettings": [],
            "expandAll": False,
            "allowLabelFilter": True,
            "allowValueFilter": True,
            "enableSorting": True,
        }
        self.gridSettings = {
            "rowHeight": 60,
            "columnWidth": 120,
            "allowReordering": True,
            "allowResizing": True,
            "allowTextWrap": True,
            "gridLines": "Both",  # Both, None, Horizontal, Vertical, Default
            "allowSelection": True,
            "selectionSettings": {
                "type": "Multiple",
                "mode": "Both",  # Row, Column, Cell, Both
            },
        }
        self.width = "100%"
        self.height = 500
        self.displayOption = {
            "view": "Both",  # Chart, Grid, Both
        }
        self.chartSettings = {
            "enableMultiAxis": True,
            "enableScrollOnMultiAxis": True,
            "primaryXAxis": {"title": "X axis title"},
            "primaryYAxis": {"title": "Y axis title"},
            "animation": {"enable": False},
            "enableExport": True,
            "chartSeries": {
                "columnHeader": "Germany-Road Bikes",
                "columnDelimiter": "-",
                "dataLabel": {
                    "visible": True,
                    "position": "Outside",
                    "connectorStyle": {
                        "width": 2,
                        "dashArray": "5,3",
                        "color": "#f4429e",
                    },
                },
                "startAngle": 270,
                "endAngle": 90,
                "explode": True,
                "enableTooltip": True,
                "border": {
                    "color": "#000",
                    "width": 2,
                },
                "type": "Column",  # Line,Column,Area,Bar,StepArea,StackingColumn,StackingArea,StackingBar,StepLine,Pareto,Bubble,Scatter,Spline,SplineArea,StackingColumn100,StackingBar100,StackingArea100,Polar,Radar,Pie,Doughnut,Funnel,Pyramid,
            },
        }
        self.editSettings = {
            "allowAdding": True,
            "allowDeleting": True,
            "allowEditing": True,
            "allowCommandColumns": True,
            "allowInlineEditing": True,
            "mode": "Batch",  # Normal,Dialog,Batch,Command Columns
        }
        self.showToolbar = True
        self.toolbar = [
            "New",
            "Save",
            "SaveAs",
            "Rename",
            "Remove",
            "Load",
            "Grid",
            "Chart",
            "Export",
            "SubTotal",
            "GrandTotal",
            "ConditionalFormatting",
            "FieldList",
        ]
        self.chartTypes = [
            "Line",
            "Column",
            "Area",
            "Bar",
            "StepArea",
            "StackingColumn",
            "StackingArea",
            "StackingBar",
            "StepLine",
            "Pareto",
            "Bubble",
            "Scatter",
            "Spline",
            "SplineArea",
            "StackingColumn100",
            "StackingBar100",
            "StackingArea100",
            "Polar",
            "Radar",
            "Pie",
            "Doughnut",
            "Funnel",
            "Pyramid",
        ]

    def registerLicense(self, key: str):
        self.__license_key = key


# Example usage
if __name__ == "__main__":
    st.title("Syncfusion Pivot Grid in Streamlit")

    data = pd.DataFrame(
        [
            {
                "Sold": 31,
                "Amount": 52824,
                "Country": "France",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q1",
            },
            {
                "Sold": 51,
                "Amount": 86904,
                "Country": "France",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q2",
            },
            {
                "Sold": 90,
                "Amount": 153360,
                "Country": "France",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q3",
            },
            {
                "Sold": 25,
                "Amount": 42600,
                "Country": "France",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q4",
            },
            {
                "Sold": 27,
                "Amount": 46008,
                "Country": "France",
                "Products": "Mountain Bikes",
                "Year": "FY 2016",
                "Quarter": "Q1",
            },
            {
                "Sold": 31,
                "Amount": 52824,
                "Country": "USA",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q1",
            },
            {
                "Sold": 51,
                "Amount": 86904,
                "Country": "USA",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q2",
            },
            {
                "Sold": 90,
                "Amount": 153360,
                "Country": "USA",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q3",
            },
            {
                "Sold": 25,
                "Amount": 42600,
                "Country": "USA",
                "Products": "Mountain Bikes",
                "Year": "FY 2015",
                "Quarter": "Q4",
            },
            {
                "Sold": 27,
                "Amount": 46008,
                "Country": "USA",
                "Products": "Mountain Bikes",
                "Year": "FY 2016",
                "Quarter": "Q1",
            },
        ]
    )

    pivot_props = PivotGridProps(data)
    pivot_props.dataSourceSettings["columns"] = [{"name": "Year"}, {"name": "Quarter"}]
    pivot_props.dataSourceSettings["rows"] = [{"name": "Country"}, {"name": "Products"}]
    pivot_props.dataSourceSettings["values"] = [{"name": "Sold"}, {"name": "Amount"}]
    pivot_props.toolbar = [
        "New",
        "Save",
        "SaveAs",
        "Rename",
        "Remove",
        "Load",
        "Grid",
        "Chart",
        "Export",
        "SubTotal",
        "GrandTotal",
        "FieldList",
    ]
    pivot_props.registerLicense(key=os.environ.get("KEY"))

    with st.sidebar:
        st.header("Example options")

        allowConditionalFormatting = st.checkbox("Allow Conditional Formatting", False)
        pivot_props.allowConditionalFormatting = allowConditionalFormatting
        if allowConditionalFormatting:
            if "ConditionalFormatting" not in pivot_props.toolbar:
                pivot_props.toolbar.append("ConditionalFormatting")
        if not allowConditionalFormatting:
            if "ConditionalFormatting" in pivot_props.toolbar:
                pivot_props.toolbar.remove("ConditionalFormatting")

    updated_data = SfPivotGrid(Data=data, Props=pivot_props)

    st.write("Updated Data:")
    st.write(updated_data)
