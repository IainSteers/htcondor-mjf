SPECFILE = htcondor-mjf.spec
PACKAGE=$(shell grep -s '^Name'    $(SPECFILE) | sed -e 's/Name: *//')
VERSION=$(shell grep -s '^Version' $(SPECFILE) | sed -e 's/Version: *//')
PKGNAME=$(PACKAGE)-$(VERSION)
TARFILE=$(PKGNAME).tgz

all:
	#tar cvzf $(TARFILE) --exclude-vcs --transform 's,^,$(PKGNAME)/,' *
	rm -rf /tmp/$(PKGNAME)
	mkdir /tmp/$(PKGNAME)
	cp -rv * /tmp/$(PKGNAME)/
	pwd ; ls -l
	cd /tmp ; tar --exclude .svn --exclude .git -czf $(TARFILE) $(PKGNAME)
	mv /tmp/$(TARFILE) .
	rm -rf /tmp/$(PKGNAME)

clean:
	rm $(TARFILE)

srpm:   all
	rpmbuild -bs --define '_sourcedir $(PWD)' ${SPECFILE}

rpm:   all
	rpmbuild -ba --define '_sourcedir $(PWD)' ${SPECFILE}
