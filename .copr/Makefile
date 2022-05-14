srpm:
	dnf install -y mock
	mock --enable-network --isolation=simple --buildsrpm --spec $(spec) --resultdir=$(outdir)
