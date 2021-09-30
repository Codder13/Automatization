$myHost = $Env:UserName

$Desktop =  $Env:ComputerName

$User = @" 
   ${Desktop}\${myHost}
"@

$location = @" 
C:\Program Files (x86)\File Organizer\resources\main.exe
"@

$action = New-ScheduledTaskAction -Execute $location -Argument $location

$trigger =  New-ScheduledTaskTrigger -AtLogOn -User $User

Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "File Organizer"