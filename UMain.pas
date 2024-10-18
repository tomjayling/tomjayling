unit UMain;

interface

uses
  USeason, UPlayerTeam, MatchEngine, ULeagueGraphic,
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, UDM, Data.DB, Vcl.Grids,
  Vcl.DBGrids;

type
  TMainForm = class(TForm)
    PlayerGrid: TDBGrid;
    NewGameBtn: TButton;
    ExitBtn: TButton;
    UsernameEdit: TEdit;
    procedure NewGameBtnClick(Sender: TObject);
    procedure ExitBtnClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.dfm}

uses UFormationGraphic;


procedure TMainForm.ExitBtnClick(Sender: TObject);
begin
  MainForm.Destroy;
end;


procedure TMainForm.NewGameBtnClick(Sender: TObject);
var
  i: Integer;
begin
  LeagueForm.Season1:=Season.Create(UsernameEdit.Text);
  FormationGraphicForm.CurrentTeamLbl.Caption := LeagueForm.Season1.TeamsIndex(0).ClubName;
  FormationGraphicForm.GetDefault(1);
  for i := 0 to 19 do FormationGraphicForm.TTMenu.Items.Add(LeagueForm.Season1.TeamsIndex(i).ClubName);
  FormationGraphicForm.Show;
end;

end.
