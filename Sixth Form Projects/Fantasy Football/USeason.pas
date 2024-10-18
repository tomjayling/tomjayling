unit USeason;

interface
uses UPlayerTeam, UDM, System.SysUtils;
type
Season = class
  private
    Username : string;
    Week : integer;
    Teams : array[0..19] of Team;
  public
    premTeams : array[0..19] of string;
    constructor Create(u: string);
    function TeamsIndex(a: integer):Team;
    function getNextWeek: integer;
end;

implementation

{ Season }



function Season.getNextWeek: integer;
begin
  inc(Week);
  result := Week;
end;

function Season.TeamsIndex(a: integer): Team;
begin
  result := Teams[a];
end;

{ Season }

constructor Season.Create(u: string);
var
  i: Integer;
begin
  username := u;
  premTeams[0] := 'Arsenal';
  premTeams[1] := 'Bournemouth';
  premTeams[2] := 'Brighton';
  premTeams[3] := 'Burnley';
  premTeams[4] := 'Cardiff';
  premTeams[5] := 'Chelsea';
  premTeams[6] := 'Crystal Palace';
  premTeams[7] := 'Everton';
  premTeams[8] := 'Fulham';
  premTeams[9] := 'Huddersfield';
  premTeams[10] := 'Leicester';
  premTeams[11] := 'Liverpool';
  premTeams[12] := 'Man City';
  premTeams[13] := 'Man United';
  premTeams[14] := 'Newcastle';
  premTeams[15] := 'Southampton';
  premTeams[16] := 'Tottenham';
  premTeams[17] := 'Watford';
  premTeams[18] := 'West Ham';
  premTeams[19] := 'Wolves';
  for i := 0 to 19 do
    begin
      Teams[i] := Team.Create(PremTeams[i]);
    end;
  Week := 0;
  end;

end.
