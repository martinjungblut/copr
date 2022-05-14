srpm:
	dnf install -y rpmdevtools rpm-build
	spectool -g -R $(spec)
	rpmbuild -bs $(spec)
