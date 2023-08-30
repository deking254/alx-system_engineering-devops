#configure ngix server
package {'nginx':
ensure => installed
}
file {'/etc/nginx/sites-enabled/default':
content => "server {
	listen 80;
	root /var/www/html;
	server_name _;
	location / {
		return 404 'Ceci n\\'est pas une page

'; }
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
}
}"
}
exec {'nginx restart':
command => 'sudo service nginx restart',
path    => '/usr/bin',
}
