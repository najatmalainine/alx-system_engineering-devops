# using Puppet set up your client SSH configuration file so that
# you can connect to a server without typing a password

file { '/home/your_username/.ssh/config':
  ensure  => present,
  content => '
    Host 34.207.63.215
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ',
  mode    => '0600',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}
