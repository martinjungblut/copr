srpm:
	mock --enable-network --buildsrpm --spec seergdb.spec
chroot-init:
	mock -r fedora-37-x86_64 --init
chroot-clean:
	mock -r fedora-37-x86_64 --clean
build: srpm
	cp /var/lib/mock/fedora-37-x86_64/result/seergdb-1.15-1.fc37.src.rpm .
	mock -r fedora-37-x86_64 --rebuild seergdb-1.15-1.fc37.src.rpm
