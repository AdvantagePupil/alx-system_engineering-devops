# A puppet manuscript to replace a line in a file on a server

$edit_file = '/var/www/html/wp-settings.php'

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${edit_file}",
  path    => ['/bin','/usr/bin']
}
