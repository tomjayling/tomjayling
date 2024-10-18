unit MatchEngine;

interface

uses
  UPlayerTeam, UDM,
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls;

type
  TMatchEngineForm = class(TForm)
    ALbl: TLabel;
    BLbl: TLabel;
    StartBtn: TButton;
    AScoreLbl: TLabel;
    BScoreLbl: TLabel;
    procedure StartBtnClick(Sender: TObject);
  private
    { Private declarations }
  public
  procedure FormCreate(Sender: TObject);
  end;

var
  MatchEngineForm: TMatchEngineForm;
  TeamA, TeamB : Team;

implementation

{$R *.dfm}

{ TForm1 }

procedure TMatchEngineForm.FormCreate(Sender: TObject);
begin
  ALbl.Caption := 'Arsenal';
  BLbl.Caption := 'Barcelona';
  AScoreLbl.Caption := '0';
  BScoreLbl.Caption := '0';
  StartBtn.Enabled := true;
end;

procedure TMatchEngineForm.StartBtnClick(Sender: TObject);
var
a,b : Team;
RatingA,RatingB,
Agoals, Bgoals : integer;
  i: Integer;
begin
  a := Team.Create('Arsenal');
  b := Team.Create('Barcelona');
  Albl.Caption := 'Arsenal';
  Blbl.caption := 'Barcelona';
  RatingA := 0;
  RatingB := 0;
//  Bgoals := trunc(b.GetXG(0.8,5.00)+a.GetXC(0.7,3));
//  Agoals := trunc(a.GetXG(0.5,3)+b.GetXC(0.2,5));
  for i := 1 to 11 do
  begin
    RatingA := RatingA + UDM.S.PlayerSet.Lookup('Surname',TeamA.PlayerIndex(i).surname,'Rating');
    RatingB := RatingB + UDM.S.PlayerSet.Lookup('Surname',TeamB.PlayerIndex(i).surname,'Rating');
  end;
  if RatingA > RatingB then
  begin
    Agoals := RatingA - RatingB;
    Bgoals := 0;
  end
  else
  begin
    Bgoals := RatingB -RatingA;
    Agoals := 0
  end;
    AScorelbl.Caption := IntToStr(Agoals);
  BScorelbl.Caption := IntToStr(Bgoals);
  StartBtn.Enabled := false;
end;

end.
