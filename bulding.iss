[Setup]
AppName=Diplom
AppVersion=1.0
DefaultDirName={autopf}\Diplom
DefaultGroupName=Diplom
OutputDir=output
OutputBaseFilename=Diplom_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=app\static\icon\icon.ico
UninstallDisplayIcon={app}\Diplom.exe
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\Diplom.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "app\static\*"; DestDir: "{app}\static"; Flags: recursesubdirs
Source: "app\ui\*"; DestDir: "{app}\ui"; Flags: recursesubdirs
Source: "app\db\db.db"; DestDir: "{app}\db"; Flags: ignoreversion

[Icons]
Name: "{group}\Diplom"; Filename: "{app}\Diplom.exe"
Name: "{userdesktop}\Diplom"; Filename: "{app}\Diplom.exe"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Run]
Filename: "{app}\Diplom.exe"; Description: "{cm:LaunchProgram,Diplom}"; Flags: nowait postinstall skipifsilent