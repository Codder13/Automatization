$myHost = $Env:UserName

$Desktop =  $Env:ComputerName

$User = @" 
   ${Desktop}\${myHost}
"@

$location = @" 
C:\Users\${myHost}\Downloads\.Folders\Organizer.exe
"@

$action = New-ScheduledTaskAction -Execute $location -Argument $location

$trigger =  New-ScheduledTaskTrigger -AtLogOn -User $User

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "File Organizer"