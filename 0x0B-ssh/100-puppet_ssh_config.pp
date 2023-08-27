#makes sure that the config file is present
file {'/etc/ssh/ssh_config.d/r.conf':
ensure  => present,
mode    => '0600',
content => 'PasswordAuthentication no
IdentityFile ~/.ssh/school'
}
