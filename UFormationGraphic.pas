unit UFormationGraphic;

interface

uses
  UMain, UPlayerTeam, UDM, ULeagueGraphic, USeason,
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.Menus, Vcl.ExtCtrls, Data.DB, Data.Win.ADODB,
  Vcl.DBCtrls;

type
  TFormationGraphicForm = class(TForm)
    GKMenu: TComboBox;
    RBMenu: TComboBox;
    CBMenu2: TComboBox;
    CBMenu1: TComboBox;
    LBMenu: TComboBox;
    MFMenu1: TComboBox;
    MFMenu2: TComboBox;
    MFMenu3: TComboBox;
    LWMenu: TComboBox;
    STMenu: TComboBox;
    RWMenu: TComboBox;
    TSBtn: TButton;
    TCBtn: TButton;
    TransferRG: TRadioGroup;
    RunBtn: TButton;
    CancelTransferBtn: TButton;
    CLineupBtn: TButton;
    RLineupBtn: TButton;
    TPMenu: TComboBox;
    TransferBtn: TButton;
    TTMenu: TComboBox;
    ELineupBtn: TButton;
    CBMenu3: TComboBox;
    SSMenu: TComboBox;
    FormationMenu: TComboBox;
    TutorialBx: TListBox;
    CurrentTeamLbl: TLabel;
    NextTeamBtn: TButton;
    PreviousTeamBTn: TButton;
    procedure FormCreate(Sender:TObject);
    procedure TeamSelectMenuChange(Sender: TObject);
    procedure RunBtnClick(Sender: TObject);
    procedure CancelTransferBtnClick(Sender: TObject);
    procedure CLineupBtnClick(Sender: TObject);
    procedure RLineupBtnClick(Sender: TObject);
    procedure TPMenuChange(Sender: TObject);
    procedure TransferBtnClick(Sender: TObject);
    procedure TTMenuChange(Sender: TObject);
    procedure ELineupBtnClick(Sender: TObject);
    procedure FormationMenuChange(Sender: TObject);
    procedure GetDefault(a: integer);
    procedure GetConfirmed(a: integer);
    procedure GetSquadPlayers(a: integer);
    procedure SaveLineup(x: integer);
    procedure TSBtnClick(Sender: TObject);
    procedure TransferRGClick(Sender: TObject);
    procedure TCBtnClick(Sender: TObject);
    procedure NextTeamBtnClick(Sender: TObject);
    procedure PreviousTeamBTnClick(Sender: TObject);
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FormationGraphicForm: TFormationGraphicForm;
  Team1 : Team;

implementation

{$R *.dfm}

{ TForm1 }


procedure TFormationGraphicForm.RunBtnClick(Sender: TObject);
var
  i,x: Integer;
  j: Integer;
begin
   x := 0;
  for i := 0 to 19 do
    begin
      if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
        x:=i;
    end;
  for j := x to 19 do
  begin
    getDefault(j+1);
    SaveLineup(j);
  end;
  LeagueForm.Show;
  hide;
end;

procedure TFormationGraphicForm.CLineupBtnClick(Sender: TObject);
var
  i,x: Integer;
begin
  x := 0;
  for i := 0 to 19 do
    begin
      if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
        x:= i;
    end;
  if x < 19 then NextTeamBtn.Enabled := true;
  RunBtn.Enabled := true;
  CLineupBtn.Enabled := false;
  RLineupBtn.Enabled := false;
  TransferBtn.Enabled := false;
  ELineupBtn.Enabled := true;
  GKMenu.Enabled := false;
  LBMenu.Enabled := false;
  CBMenu1.Enabled := false;
  CBMenu2.Enabled := false;
  CBMenu3.Enabled := false;
  RBMenu.Enabled := false;
  MFMenu1.Enabled := false;
  MFMenu2.Enabled := false;
  MFMenu3.Enabled := false;
  LWMenu.Enabled := false;
  RWMenu.Enabled := false;
  STMenu.Enabled := false;
  SSMenu.Enabled := false;
  SaveLineup(x);
end;

procedure TFormationGraphicForm.TTMenuChange(Sender: TObject);
begin
  TSBtn.Enabled := true;
  with S.PlayerSet do
  begin
    filtered := false;
    filter := 'Position = ' + intToStr(TPMenu.ItemIndex + 1) + ' and TeamID = ' + intToStr(TTMenu.ItemIndex+1);
    filtered := true;
  end;
  S.PlayerSet.First;
  while not S.PlayerSet.Eof do
  begin
    s.PlayerSet.Next;
  end;
  TutorialBx.Clear;
  TutorialBx.Items.Add('Select search to browse players');
end;

procedure TFormationGraphicForm.TSBtnClick(Sender: TObject);
var
Selected: boolean;
  i,x,y: Integer;
begin
  TransferRG.Items.Clear;
  S.PlayerSet.First;
  for i := 0 to 19 do
  begin
  if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
  begin
    x := i;
  end;
  end;
  y := S.PlayerSet['TeamID']-1;
  while not S.PlayerSet.Eof do
  begin
    Selected := false;
    if y < x then
    begin
      for i := 0 to 10 do
      begin
        if LeagueForm.Season1.TeamsIndex(y).PlayerIndex(i).surname = S.PlayerSet['second_name'] then
        begin
          Selected := true;
        end;
      end;
    end;
    if not Selected then
    begin
      TransferRG.Items.Add(S.PlayerSet['second_name']);
    end;
    s.PlayerSet.Next;
  end;
  TutorialBx.Clear;
  TutorialBX.Items.Add('Tick the player you want to transfer');
  TutorialBx.Items.Add('Then press confirm transfer')
end;

procedure TFormationGraphicForm.TPMenuChange(Sender: TObject);
begin
  TTMenu.Enabled := true;
  TutorialBx.Items.Add('Select team');
end;


procedure TFormationGraphicForm.RLineupBtnClick(Sender: TObject);
var
i,x:integer;
begin
   x := 0;
  for i := 0 to 19 do
    begin
      if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
        x:= i + 1;
    end;
  getDefault(x+1);
  GKMenu.Enabled := false;
  LBMenu.Enabled := false;
  CBMenu1.Enabled := false;
  CBMenu2.Enabled := false;
  CBMenu3.Enabled := false;
  RBMenu.Enabled := false;
  MFMenu1.Enabled := false;
  MFMenu2.Enabled := false;
  MFMenu3.Enabled := false;
  LWMenu.Enabled := false;
  RWMenu.Enabled := false;
  STMenu.Enabled := false;
  SSMenu.Enabled := false;
  TransferBtn.Enabled := false;
  RLineupBtn.Enabled := false;
  CLineupBtn.Enabled := false;
  TutorialBx.Clear;
  TutorialBx.Items.Add('Select a team to edit');
end;

procedure TFormationGraphicForm.TransferBtnClick(Sender: TObject);
begin
  TPMenu.Enabled := true;
  CancelTransferBtn.Enabled := true;
  RLineupBtn.Enabled := false;
  CLineupBtn.Enabled := false;
  TransferBtn.Enabled := false;
  TutorialBx.Clear;
  TutorialBx.Items.Add('Select a position to start');
  TutorialBx.Items.Add('Note: if you want to transfer a player make sure they are');
  TutorialBx.Items.Add('not already confirmed for another team. If so go back and');
  TutorialBx.Items.Add('edit the team they belong to');
end;

procedure TFormationGraphicForm.TransferRGClick(Sender: TObject);
begin
  TCBtn.Enabled := true;
end;

procedure TFormationGraphicForm.ELineupBtnClick(Sender: TObject);
var
i,x :integer;
begin
  RunBtn.Enabled := false;
  RLineupBtn.Enabled := true;
  CLineupBtn.Enabled := true;
  TransferBtn.Enabled := true;
  ELineupBtn.Enabled := false;
  GKMenu.Enabled := true;
  LBMenu.Enabled := true;
  CBMenu1.Enabled := true;
  CBMenu2.Enabled := true;
  CBMenu3.Enabled := true;
  RBMenu.Enabled := true;
  MFMenu1.Enabled := true;
  MFMenu2.Enabled := true;
  MFMenu3.Enabled := true;
  LWMenu.Enabled := true;
  RWMenu.Enabled := true;
  STMenu.Enabled := true;
  SSMenu.Enabled := true;
  FormationMenu.Enabled := true;
  for i := 0 to 19 do
    begin
      if leagueform.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
      x := i+1;
    end;
  GetSquadPlayers(x);
  TutorialBx.Clear;
  TutorialBx.Items.Add('Use the drop down menus to change players,');
  TutorialBx.Items.Add('Change your formation with the formation menu');
  Tutorialbx.Items.Add('When you are finished click "Confirm Lineup"');
end;

procedure TFormationGraphicForm.CancelTransferBtnClick(Sender: TObject);
begin
 TransferBtn.Enabled := true;
 RLineupBtn.Enabled := true;
 CLineupBtn.Enabled := true;
 TPMenu.Enabled := false;
 TTMenu.Enabled := false;
 TSBtn.Enabled := false;
 CancelTransferBtn.Enabled := false;
 S.PlayerSet.Filtered := false;
end;



procedure TFormationGraphicForm.FormationMenuChange(Sender: TObject);
begin
  case FormationMenu.ItemIndex of
    0: begin
      CBMenu3.Hide;
      SSMenu.Hide;
      MFMenu3.Show;
      LWMenu.Show;
      RWMenu.Show;
    end;
    1: begin
      CBMenu3.Hide;
      SSMenu.Show;
      MFMenu3.Hide;
      LWMenu.Show;
      RWMenu.Show;
    end;
    2: begin
      CBMenu3.Show;
      SSMenu.Show;
      MFMenu3.Show;
      RWMenu.Hide;
      LWMenu.Hide;
    end;
    3: begin
      CBMenu3.Show;
      SSMenu.Hide;
      MFMenu3.Hide;
      RWMenu.Show;
      LWMenu.Show;
    end;
  end;
end;

procedure TFormationGraphicForm.FormCreate(Sender: TObject);
var
  i: Integer;
begin
  CBMenu3.Hide;
  SSMenu.Hide;
  GKMenu.Clear;
  LBMenu.Clear;
  RBMenu.Clear;
  CBMenu1.Clear;
  CBMenu2.Clear;
  MFMenu1.Clear;
  MFMenu2.Clear;
  MFMenu3.Clear;
  LWMenu.Clear;
  RWMenu.Clear;
  STMenu.Clear;
  GKMenu.Text := 'GoalKeeper';
  LBMenu.Text := 'LeftBack';
  RBMenu.Text := 'RightBack';
  CBMenu1.Text := 'CentreBack';
  CBMenu2.Text := 'CentreBack';
  CBMenu3.Text := 'CentreBack';
  MFMenu1.Text := 'Midfielder';
  MFMenu2.Text := 'Midfielder';
  MFMenu3.Text := 'Midfielder';
  LWMenu.Text := 'LeftWinger';
  RWMenu.Text := 'RightWinger';
  STMenu.Text := 'Striker';
  SSMenu.Text := 'Second Striker';
  GKMenu.Enabled := false;
  LBMenu.Enabled := false;
  CBMenu1.Enabled := false;
  CBMenu2.Enabled := false;
  CBMenu3.Enabled := false;
  RBMenu.Enabled := false;
  MFMenu1.Enabled := false;
  MFMenu2.Enabled := false;
  MFMenu3.Enabled := false;
  LWMenu.Enabled := false;
  RWMenu.Enabled := false;
  STMenu.Enabled := false;
  SSMenu.Enabled := false;
  ELineupBtn.Enabled := true;
  CLineupBtn.Enabled := true;
  RLineupBtn.Enabled := false;
 // NextTeamBtn.Enabled := false;
  PreviousTeamBtn.Enabled := false;
  FormationMenu.Enabled := false;
  TransferBtn.Enabled := false;
  TPMenu.Enabled := false;
  TTMenu.Enabled := false;
  TSBtn.Enabled := false;
  TCBtn.Enabled := false;
  CancelTransferBtn.Enabled := false;
  TransferRG.Items.Clear;
  RunBtn.Enabled := true;
  TPMenu.Items.Add('Goal Keeper');
  TPMenu.Items.Add('Defender');
  TPMenu.Items.Add('Midfielder');
  TPMenu.Items.Add('Forward');
  FormationMenu.Items.Add('433');
  FormationMenu.Items.Add('424');
  FormationMenu.Items.Add('532');
  FormationMenu.Items.Add('523');
  TutorialBx.Items.Add('Welcome to the team selector!');
  TutorialBx.Items.Add('Confirm your team lineup to move onto the next team');
  TutorialBx.Items.Add('press run when you have edited all the teams you want');
  Hide;
end;

procedure TFormationGraphicForm.GetConfirmed(a: integer);
var
d,m,f, i: integer;
playerX: Player;
begin
  d:= 0;
  m := 0;
  f := 0;
  for i := 0 to 10 do
  begin
    playerX := LeagueForm.Season1.TeamsIndex(a).PlayerIndex(i);
      case playerX.position of
        1: GKMenu.Text := playerX.surname;
        2: begin
           inc(d);
           case d of
           1: LBMenu.Text := playerX.surname;
           2: RBMenu.Text := playerX.surname;
           3: CBMenu1.Text := playerX.surname;
           4: CBMenu2.Text := playerX.surname;
           5: CBMenu3.Text := playerX.surname;
           end;
        end;
        3: begin
           inc(m);
           case m of
           1: MFMenu2.Text := playerX.surname;
           2: MFMenu1.Text := playerX.surname;
           3: MFMenu3.Text := playerX.surname;
           end;
        end;
        4: begin
          inc(f);
          case f of
           1: STMenu.Text := playerX.surname;
           2: SSMenu.Text := playerX.surname;
           3: begin
              LWMenu.Text := SSMenu.Text;
              SSMenu.Text := '';
              RWMenu.Text := playerX.surname;
           end;
           4: begin
              SSMenu.Text := LWMenu.Text;
              LWMenu.Text := RWMenu.Text;
              RWMenu.Text := playerX.surname;
           end;
           end;
        end;
      end;
    S.PlayerSet.Prior;
  end;
  if d=4 then
  begin
    if m=3 then
    begin
      CBMenu3.Hide;
      SSMenu.Hide;
      MFMenu3.Show;
      LWMenu.Show;
      RWMenu.Show;
    end
    else
    begin
      CBMenu3.Hide;
      SSMenu.Show;
      MFMenu3.Hide;
      LWMenu.Show;
      RWMenu.Show;
    end;
  end
  else
  begin
    if m=3 then
    begin
      CBMenu3.Show;
      SSMenu.Show;
      MFMenu3.Show;
      RWMenu.Hide;
      LWMenu.Hide;
    end
    else
    begin
      CBMenu3.Show;
      SSMenu.Hide;
      MFMenu3.Hide;
      RWMenu.Show;
      LWMenu.Show;
    end;
  end;
  FormationMenu.Text := intToStr(d) + intToStr(m) + intToStr(f);
end;

procedure TFormationGraphicForm.GetDefault(a: integer);
var
d,m,f : integer;
begin
  GKMenu.Clear;
  LBMenu.Clear;
  RBMenu.Clear;
  CBMenu1.Clear;
  CBMenu2.Clear;
  MFMenu1.Clear;
  MFMenu2.Clear;
  MFMenu3.Clear;
  LWMenu.Clear;
  RWMenu.Clear;
  STMenu.Clear;
  with S.PlayerSet do
  begin
    Filtered := false;
    Filter := 'TeamID = ' + intToStr(a) + ' AND ' + 'Selected = TRUE';
    Filtered := true;
    IndexFieldNames := 'goal_contributions';
    end;
  d := 0;
  m := 0;
  f := 0;
  S.PlayerSet.Last;
  while not S.PlayerSet.Bof do
  begin
      case S.PlayerSet['Position'] of
        1: GKMenu.Text := S.PlayerSet['second_name'];
        2: begin
           inc(d);
           case d of
           1: LBMenu.Text := S.PlayerSet['second_name'];
           2: RBMenu.Text := S.PlayerSet['second_name'];
           3: CBMenu1.Text := S.PlayerSet['second_name'];
           4: CBMenu2.Text := S.PlayerSet['second_name'];
           5: CBMenu3.Text := S.PlayerSet['second_name'];
           end;
        end;
        3: begin
           inc(m);
           case m of
           1: MFMenu2.Text := S.PlayerSet['second_name'];
           2: MFMenu1.Text := S.PlayerSet['second_name'];
           3: MFMenu3.Text := S.PlayerSet['second_name'];
           end;
        end;
        4: begin
          inc(f);
          case f of
           1: STMenu.Text := S.PlayerSet['second_name'];
           2: SSMenu.Text := S.PlayerSet['second_name'];
           3: begin
              LWMenu.Text := SSMenu.Text;
              SSMenu.Text := '';
              RWMenu.Text := S.PlayerSet['second_name']
           end;
           4: begin
              SSMenu.Text := LWMenu.Text;
              LWMenu.Text := RWMenu.Text;
              RWMenu.Text := S.PlayerSet['second_name'];
           end;
           end;
        end;
      end;
    S.PlayerSet.Prior;
  end;
  if d=4 then
  begin
    if m=3 then
    begin
      CBMenu3.Hide;
      SSMenu.Hide;
      MFMenu3.Show;
      LWMenu.Show;
      RWMenu.Show;
    end
    else
    begin
      CBMenu3.Hide;
      SSMenu.Show;
      MFMenu3.Hide;
      LWMenu.Show;
      RWMenu.Show;
    end;
  end
  else
  begin
    if m=3 then
    begin
      CBMenu3.Show;
      SSMenu.Show;
      MFMenu3.Show;
      RWMenu.Hide;
      LWMenu.Hide;
    end
    else
    begin
      CBMenu3.Show;
      SSMenu.Hide;
      MFMenu3.Hide;
      RWMenu.Show;
      LWMenu.Show;
    end;
  end;
  FormationMenu.Text := intToStr(d) + intToStr(m) + intToStr(f);
  S.PlayerSet.Filtered := false;
end;

procedure TFormationGraphicForm.GetSquadPlayers(a: integer);
begin
  with S.PlayerSet do
  begin
    Filtered := false;
    Filter := 'TeamID = ' + intToStr(a);
    Filtered := true;
  end;
  S.PlayerSet.Last;
  while not S.PlayerSet.Bof do
  begin
     case S.PlayerSet['Position'] of
      1: GKMenu.Items.Add(S.PlayerSet['second_name']);
      2: begin
        LBMenu.Items.Add(S.PlayerSet['second_name']);
        CBMenu1.Items.Add(S.PlayerSet['second_name']);
        CBMenu2.Items.Add(S.PlayerSet['second_name']);
        CBMenu3.Items.Add(S.PlayerSet['second_name']);
        RBMenu.Items.Add(S.PlayerSet['second_name']);
      end;
      3: begin
        MFMenu1.Items.Add(S.PlayerSet['second_name']);
        MFMenu2.Items.Add(S.PlayerSet['second_name']);
        MFMenu3.Items.Add(S.PlayerSet['second_name']);
      end;
      4: begin
        LWMenu.Items.Add(S.PlayerSet['second_name']);
        RWMenu.Items.Add(S.PlayerSet['second_name']);
        STMenu.Items.Add(S.PlayerSet['second_name']);
        SSMenu.Items.Add(S.PlayerSet['second_name']);
      end;
      end;
    S.PlayerSet.Prior;
  end;
  S.PlayerSet.Filtered := false;
end;

procedure TFormationGraphicForm.SaveLineup(x: integer);
begin
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(GKMenu.text),0);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(LBMenu.text),1);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(RBMenu.text),2);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(CBMenu1.text),3);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(CBMenu2.text),4);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(MFMenu1.text),5);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(MFMenu2.text),6);
  LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(STMenu.text),7);
  case StrToInt(FormationMenu.text[1]) of
  4: begin
     LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(LWMenu.text),9);
     LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(RWMenu.text),10);
     if StrToInt(FormationMenu.text[2]) = 3 then
       LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(MFMenu3.text),8)
     else
     LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(SSMenu.text),8);
  end;
  5: begin
     LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(CBMenu3.text),8);
     if StrToInt(FormationMenu.text[3]) = 3 then
     begin
       LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(MFMenu3.text),9);
       LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(SSMenu.text),10);
     end
     else
     begin
       LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(LWMenu.text),9);
       LeagueForm.Season1.TeamsIndex(x).addPlayer(Player.Create(RWMenu.text),10)
     end;
  end;
  end;
end;

procedure TFormationGraphicForm.NextTeamBtnClick(Sender: TObject);
var
i,x: integer;
begin
  x := 0;
  for i := 0 to 19 do
    begin
      if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
        x:= i + 1;
    end;
    CurrentTeamLbl.Caption := LeagueForm.Season1.TeamsIndex(x).ClubName;
    GetDefault(x+1);
    ELineupBtn.Enabled := true;
    CLineupBtn.Enabled := true;
   // NextTeamBtn.Enabled := false;
    PreviousTeamBtn.Enabled := true;
    TutorialBx.Clear;
    TutorialBx.Items.Add('Confirm your team lineup to advance to the next team');
end;

procedure TFormationGraphicForm.PreviousTeamBTnClick(Sender: TObject);
var
x,i: integer;
begin
  x := 0;
  for i := 0 to 19 do
    begin
      if LeagueForm.Season1.TeamsIndex(i).ClubName = CurrentTeamLbl.Caption then
        x:= i-1;
    end;
    CurrentTeamLbl.Caption := LeagueForm.Season1.TeamsIndex(x).ClubName;
    GetConfirmed(x);
    ELineupBtn.Enabled := true;
    CLineupBtn.Enabled := true;
    NextTeamBtn.Enabled := true;
    if x = 0 then
    PreviousTeamBtn.Enabled := false;
end;

procedure TFormationGraphicForm.TCBtnClick(Sender: TObject);
var
p : Player;
begin
  p := Player.Create(TransferRG.Items[TransferRG.ItemIndex]);
  case p.position of
  1: GKMenu.Items.Add(p.surname);
  2: begin
    CBMenu1.Items.Add(p.surname);
    CBMenu2.Items.Add(p.surname);
    CBMenu3.Items.Add(p.surname);
  end;
  3: begin
    MFMenu1.Items.Add(p.surname);
    MFMenu2.Items.Add(p.surname);
    MFMenu3.Items.Add(p.surname);
  end;
  4: begin
    LWMenu.Items.Add(p.surname);
    RWMenu.Items.Add(p.surname);
    SSMenu.Items.Add(p.surname);
    STMenu.Items.Add(p.surname);
  end;
  end;
end;

procedure TFormationGraphicForm.TeamSelectMenuChange(Sender: TObject);
begin
  ELineupBtn.Enabled := true;
  TutorialBx.Clear;
  TutorialBx.Items.Add('Click "Edit Lineup" to make changes');
end;



{ Notes:
-create season form with fixtures, league table and sim match
-

}

end.
