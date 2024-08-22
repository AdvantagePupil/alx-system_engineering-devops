# Increases the number of requests that nginx can handle.
# increase maximum open files limit for nginx user.

exec { 'set_ulimit_to 5000':
  command => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 5000\"/" /etc/default/nginx'

} -> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
