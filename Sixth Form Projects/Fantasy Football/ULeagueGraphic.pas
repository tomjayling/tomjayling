unit ULeagueGraphic;

interface

uses
  UDM, UPlayerTeam, USeason,
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB, Vcl.StdCtrls, Vcl.Grids,
  Vcl.DBGrids, Data.Win.ADODB;

type
  FixtureList = array[0..9,0..1] of string;
  TLeagueForm = class(TForm)
    FixtureListBx: TListBox;
    Fixtures: TLabel;
    PlayBtn: TButton;
    SkipBtn: TButton;
    LeagueGrid: TDBGrid;
    PointsBx: TListBox;
    PointsBtn: TButton;

    Procedure FormCreate(Sender: TObject);
    procedure PlayBtnClick(Sender: TObject);
    procedure PointsBtnClick(Sender: TObject);

  private
    procedure getMatchResult(a,b: string);
    function getChanceResult(t: team): integer;
    function getFixtures(a: integer): FixtureList;
    procedure UpdateTable;
    { Private declarations }
  public
    Season1:Season;
    { Public declarations }
  end;

var
  LeagueForm: TLeagueForm;

implementation

{$R *.dfm}

{ TLeagueForm }

procedure TLeagueForm.FormCreate(Sender: TObject);
begin
//  FixtureListBx.Clear;
  FixtureListBx.Items.Add('Week 1:');
  Season1:=Season.Create(' ');
//  with UDM.S.TeamQuery do
//  begin
//    Close;
//    SQL.Clear;
//    SQL.Add('Select TeamSeason.Position, Team.TeamName, TeamSeason.GoalsScored, TeamSeason.GoalsConceded, TeamSeason.GoalDifference');
//    SQL.Add('from TeamSeaason');
//    SQL.Add('inner join Team');
//    SQL.Add('on (TeamSeason.TeamID = Team.TeamID)');
//    ExecSQL;
//    Open;
//  end;
//  Hide;
end;

function TLeagueForm.getChanceResult(t: team): integer;
var
i,r2,r1 : integer;
begin
  result := 0;
  i := 0;
  r1 := random(t.totalAttack);
  while (r1 > 0) do
  begin
    inc(i);
    r1 := trunc(r1 - t.PlayerIndex(i).AttackingThreat);
    if not (r1 > 0) then
    begin
      r2 := random(100);
      if trunc(30*t.PlayerIndex(i).getXG) > r2 then
      begin
        result := 1;
        FixtureListBx.Items.Add('Goal (' + t.PlayerIndex(i).surname + ')');
      end ;
     // else
     // FixtureListBx.Items.Add('Miss (' + t.PlayerIndex(i).surname + ')');
    end;
  end;
end;

function TLeagueForm.getFixtures(a: integer): FixtureList;
var
  i,j: Integer;
  MatchWeek : FixtureList;
begin
  S.MatchSet.First;
  for i := 1 to ((a-1)*10) do
  begin
    S.MatchSet.Next;
  end;
  for j := 0 to 9 do
    begin
      MatchWeek[j,0] := S.MatchSet['Home_Team'];
      MatchWeek[j,1] := S.MatchSet['Away_Team'];
      S.MatchSet.Next;
    end;
  result := MatchWeek;
end;

procedure TLeagueForm.getMatchResult(a, b: string);
var
aChances,bChances, aGoals, bGoals: integer;
  i,j,r, r1,r2: Integer;
  Home, Away : Team;
begin
  aGoals := 0;
  bGoals := 0;
  for i := 0 to 19 do
    begin
      if Season1.TeamsIndex(i).ClubName = a then
      begin
        Home := Season1.TeamsIndex(i);
      end
      else if Season1.TeamsIndex(i).ClubName = b then
      begin
        Away := Season1.TeamsIndex(i);
      end;
    end;
  aChances := trunc(((Home.totalICT/Away.totalICT)*(Home.totalICT + Away.totalICT)) / (Away.totalDefense));
  bChances := trunc(((Away.totalICT/Home.totalICT)*(Away.totalICT + Home.totalICT)) / (Home.totalDefense));
  for i := 1 to aChances do
  begin
    aGoals := aGoals + getChanceResult(Home);
  end;
  for i := 1 to bChances do
  begin
    bGoals := bGoals + getChanceResult(Away);
  end;
  FixtureListBx.items.add(Home.ClubName + ' ' + intToStr(aGoals) + ' vs ' + intToStr(bGoals) + ' ' + Away.ClubName);
  if aGoals > bGoals then Home.UpdatePoints(3)
  else if bGoals > aGoals then Away.UpdatePoints(3)
  else
  begin
    Home.UpdatePoints(1);
    Away.UpdatePoints(1);
  end;
end;

procedure TLeagueForm.PlayBtnClick(Sender: TObject);
var
Gameweek : integer;
Fixtures : FixtureList;
  i: Integer;
begin
  FixtureListBx.Clear;
  Gameweek := Season1.getNextWeek;
  FixtureListBx.Items.Add('Week: ' + intToStr(Gameweek));
  Fixtures := getFixtures(Gameweek);
  for i := 0 to 9 do
  begin
    FixtureListBx.Items.Add(Fixtures[i,0] + ' vs ' + Fixtures[i,1]);
    getMatchResult(Fixtures[i,0],Fixtures[i,1]);
  end;
//  UpdateTable;
  end;

procedure TLeagueForm.PointsBtnClick(Sender: TObject);
var
  i: Integer;
  j: Integer;
  temp : Team;
  teams : array[0..19] of Team;
begin
  PointsBx.Clear;
  for i := 0 to 19 do
  begin
    Teams[i] := Season1.TeamsIndex(i);
    if not (i < 1) then
    begin
    for j := i downto 1 do
    begin
      if Teams[j-1].GetPoints < Teams[j].GetPoints then
      begin
        temp := Teams[j];
        Teams[j] := Teams[j-1];
        Teams[j-1] := temp;
      end;
    end;
    end;
  end;
  for i := 0 to 19 do
    begin
      PointsBx.Items.Add(intToStr(i+1) + '. ' + Teams[i].ClubName + ' ' + intToStr(Teams[i].GetPoints));
    end;
end;

procedure TLeagueForm.UpdateTable;
begin
  with S.LeagueQuery do
  begin
    First;
    Edit;
    S.LeagueQuery['Points'] := Season1.TeamsIndex(S.LeagueQuery['Team.TeamID']-1).GetPoints;
    Post;
    if not eof then
    Next;
  end;
end;

end.
