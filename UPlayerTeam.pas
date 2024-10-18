unit UPlayerTeam;

interface

uses UDM, System.SysUtils ;

type
Player = class
private
  xG,xA,form,ict, attack, defense : real;
  public
  surname : string;
  position : integer;
  constructor Create(b: string);
  function attackingThreat: real;
  function defensiveContribution: real;
  function getXG: real;
end;
TLineup = array[0..10] of Player;
Team = class
  private
  Points : integer;
  Lineup : TLineup;
  public
  ClubName : string;
  constructor Create(a : string);
  function totalAttack: integer;
  function totalDefense: integer;
  function totalICT: integer;
  function PlayerIndex(i: integer): Player;
//  function getDefaultLineup(a: string): TLineup;
//  procedure OptimiseLineup(a: string;l:TLineup);
  procedure addPlayer(p : Player;i: integer);
  procedure UpdatePoints(a : integer);
end;

implementation

{ Player }

function Player.attackingThreat: real;
begin
  result := attack;
end;

constructor Player.Create(b: string);
begin
  surname := b;
  UDM.S.PlayerSet.First;
  while not UDM.S.PlayerSet.Eof do
  begin
    if UDM.S.PlayerSet['second_name'] = b then
    begin
      position := S.PlayerSet['Position'];
      xG := 90*(S.PlayerSet['xG']/S.PlayerSet['minutes']);
      xA := 90*(S.PlayerSet['xA']/S.PlayerSet['minutes']);
      defense := (3420 div 4)* (S.PlayerSet['clean_sheets'])/(S.PlayerSet['minutes']);
      attack := S.PlayerSet['threat'];
      ict := S.PlayerSet['ict_index']div 100;
    end;
    UDM.S.PlayerSet.Next;
  end;
  if xG = 0 then xG := 0.5;
  if xA = 0 then xA := 0.5;
  if defense = 0 then defense := 1;
  end;

function Player.defensiveContribution: real;
begin
  result := defense;
end;


function Player.getXG: real;
begin
  result := xG;
end;

{ Team }


procedure Team.addPlayer(p : Player;i: integer);
begin
  Lineup[i] := p;
end;

constructor Team.Create(a: string);
begin
  ClubName := a;
  Points := 0;
end;

//function Team.getDefaultLineup(a : string): TLineup;
//var
//  i,j,x: Integer;
//  pNames : array[0..10] of String;
//  k: Integer;
//begin
//  x := 0;
//  for i := 1 to 4 do
//  begin
//     with S.PlayerQuery do
//      begin
//        Close;
//        Parameters.ParamByName('PlayerPos').Value := i;
//        Parameters.ParamByName('PlayerTeamName').Value := ClubName;
//        Open;
//      end;
//     S.PlayerQuery.First;
//     for j := 1 to StrToInt(a[i]) do
//     begin
//       pNames[x] := S.PlayerQuery['second_name'];
//       S.PlayerQuery.Edit;
//       S.PlayerQuery['Selected'] := true;
//       S.PlayerSet.
//       S.PlayerQuery.Next;
//     end;
//  end;
//  for k := 0 to 11 do
//  begin
//    result[k] := Player.Create(pNames[k]);
//  end;
//end;

//procedure Team.OptimiseLineup(a: string;l: TLineup);
//begin
//
//end;

function Team.PlayerIndex(i: integer): Player;
begin
  result := Lineup[i];
end;

function Team.totalAttack: integer;
var
  i: Integer;
begin
  result := 0;
  for i := 1 to 10 do
  begin
    result := result + trunc(Lineup[i].attackingThreat);
  end;
end;

function Team.totalDefense: integer;
var
  i: Integer;
  totdefence:integer;
begin
  totdefence:=0;
  for i := 0 to 5 do
  begin
    totdefence := totdefence + trunc(Lineup[i].defensiveContribution);
  end;
  result:=totdefence div 6;
  if result = 0 then result:= 1;
end;

function Team.totalICT: integer;
var
  i: Integer;
  totICT:integer;
begin
  totICT := 0;
  for i := 1 to 10 do
  begin
    totICT := totICT + trunc(Lineup[i].ict);
  end;
  result:=totICT;
end;

procedure Team.UpdatePoints(a: integer);
begin
  Points := Points + a;
end;

end.
