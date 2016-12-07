#!/bin/bash
rpmbuild --define "_topdir `pwd`" -ba SPECS/tomcat.spec

