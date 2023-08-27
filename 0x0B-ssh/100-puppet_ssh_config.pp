file {'/etc/ssh/ssh_config.d/r':
ensure  => present,
mode    => '0600',
content => 'PasswordAuthentication no
IdentityFile ~/.ssh/school'
}
