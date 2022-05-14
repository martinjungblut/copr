srpm:
	dnf install -y mock rpmdevtools
	spectool -g -R $(spec)
	mock --buildsrpm --spec $(spec) --resultdir=$(outdir)
