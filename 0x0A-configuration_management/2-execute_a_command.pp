#kills the a process called killmenow
exec {'killmenow':
path    => '/bin',
command => 'pkill killmenow'
}
