# install flask from pip3

exec { 'install python packages':
  command => '/usr/bin/pip3 install flask -v 2.1.0',
}
