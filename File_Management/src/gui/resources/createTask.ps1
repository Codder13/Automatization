$myHost = $Env:UserName

$Desktop =  $Env:ComputerName

$User = @" 
   ${Desktop}\${myHost}
"@

$location = @" 
C:\Users\${myHost}\AppData\Roaming\File Organizer\sort.exe
"@

$action = New-ScheduledTaskAction -Execute $location -Argument $location

$trigger =  New-ScheduledTaskTrigger -AtLogOn -User $User

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "File Organizer"