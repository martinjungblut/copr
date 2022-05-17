srpm:
	mock --enable-network --buildsrpm --spec racket.spec
chroot-init:
	mock -r fedora-35-x86_64 --init
chroot-clean:
	mock -r fedora-35-x86_64 --clean
build: srpm
	cp /var/lib/mock/fedora-35-x86_64/result/racket-8.5-1.fc35.src.rpm .
	mock -r fedora-35-x86_64 --rebuild racket-8.5-1.fc35.src.rpm
