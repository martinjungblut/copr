srpm:
	dnf install -y rpmdevtools rpm-build
	spectool -g -R $(spec)
	rpmbuild -bs $(spec)
	mv /builddir/build/SRPMS/*.src.rpm $(outdir)
