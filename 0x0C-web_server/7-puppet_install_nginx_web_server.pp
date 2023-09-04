#configure ngix server
package {'nginx':
ensure => installed
}
file {'/var/www/html/404.html':
ensure  => present,
content => "Ceci n'est pas une page
",
}
file {'/var/www/html/index.html':
ensure  => present,
content => "Hello World!
",
}
file {'/etc/nginx/sites-enabled/default':
content => "server {
	listen 80;
	root /var/www/html;
	server_name _;
	error_page 404 /404.html;
	index index.html;
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
}
}"
}
