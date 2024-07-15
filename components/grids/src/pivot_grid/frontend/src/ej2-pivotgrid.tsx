import { StreamlitComponentBase, withStreamlitConnection, Streamlit } from "streamlit-component-lib";
import React, { ReactNode } from "react";
import { PivotViewComponent, Inject, FieldList, GroupingBar, Toolbar, PDFExport, ExcelExport, ConditionalFormatting, CalculatedField } from '@syncfusion/ej2-react-pivotview';
import { registerLicense } from "@syncfusion/ej2-base";
import { ClickEventArgs } from "@syncfusion/ej2-navigations";

/**
 * This is Syncfusion Streamlit Pivot Grid component.
 */
class EJ2PivotGrid extends StreamlitComponentBase<{}> {
  private pivotGridInstance: PivotViewComponent | null = null;

  constructor(props: any) {
    super(props);
    this.state = { refreshed: 1 };
  }

  toolbarClick = (args: ClickEventArgs): void => {
    switch (args.item.text) {
      case 'PDF Export':
        this.pivotGridInstance?.pdfExport();
        break;
      case 'Excel Export':
        this.pivotGridInstance?.excelExport();
        break;
      case 'CSV Export':
        this.pivotGridInstance?.csvExport();
        break;
    }
  }

  dataBound = (): void => {
    if (this.pivotGridInstance) {
      const gridData = this.pivotGridInstance.engineModule.data;
      Streamlit.setComponentValue(gridData);
    }
  }

  onActionComplete = (): void => {
    if (this.pivotGridInstance) {
      const gridData = this.pivotGridInstance.engineModule.data;
      Streamlit.setComponentValue(gridData);
    }
  }

  componentWillReceiveProps(nextProps: any) {
    if (nextProps.args.params.data !== this.props.args.params.data) {
      if (this.pivotGridInstance) {
        this.pivotGridInstance.dataSourceSettings.dataSource = nextProps.args.params.data;
        this.pivotGridInstance.refresh();
      }
    }
  }

  render(): ReactNode {
    const { 
      data,
      licenseKey,
      theme,
      dataSourceSettings,
      gridSettings,
      chartSettings,
      editSettings,
      toolbar,
      showToolbar,
      allowExcelExport,
      allowPdfExport,
      allowConditionalFormatting,
      showGroupingBar,
      allowDeferLayoutUpdate,
      allowCalculatedField,
      allowDrillThrough,
      showFieldList,
      height,
      width,
      displayOption,
      chartTypes,
    } = this.props.args.params;

    if (licenseKey) {
      registerLicense(licenseKey);
    }

    return (
      <>
        <link rel="stylesheet" href={theme} />
        <PivotViewComponent ref={pivotGrid => this.pivotGridInstance = pivotGrid}
          dataSourceSettings={dataSourceSettings}
          gridSettings={gridSettings}
          chartSettings={chartSettings}
          editSettings={editSettings}
          toolbar={toolbar}
          showToolbar={showToolbar}
          allowExcelExport={allowExcelExport}
          allowPdfExport={allowPdfExport}
          toolbarClick={this.toolbarClick.bind(this)}
          dataBound={this.dataBound}
          actionComplete={this.onActionComplete}
          allowConditionalFormatting={allowConditionalFormatting}
          showGroupingBar={showGroupingBar}
          allowDeferLayoutUpdate={allowDeferLayoutUpdate}
          allowCalculatedField={allowCalculatedField}
          allowDrillThrough={allowDrillThrough}
          showFieldList={showFieldList}
          height={height}
          width={width}
          displayOption={displayOption}
          chartTypes={chartTypes}
          >
          <Inject services={[FieldList, GroupingBar, Toolbar, PDFExport, ExcelExport, ConditionalFormatting, CalculatedField]} />
        </PivotViewComponent>
      </>
    );
  }
}

export default withStreamlitConnection(EJ2PivotGrid);
