unit UDM;

interface

uses
  System.SysUtils, System.Classes, Data.DB, Data.Win.ADODB;

type
  TS = class(TDataModule)
    miaConn: TADOConnection;
    PlayerSource: TDataSource;
    PlayerSet: TADODataSet;
    LeagueTable: TADODataSet;
    MatchSet: TADODataSet;
    TableSource: TDataSource;
    LeagueQuery: TADOQuery;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  S: TS;

implementation

{%CLASSGROUP 'Vcl.Controls.TControl'}

{$R *.dfm}

end.
