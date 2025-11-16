all:
	publish

publish:
	rsync -aOPvhe ssh --delete --exclude-from=.exclude ./ harish@metroplex:/var/www/v5.harishnarayanan.org

install: publish

checklinks:
	wget --spider -o wget.log -e robots=off -w 1 -r -p https://v5.harishnarayanan.org/
