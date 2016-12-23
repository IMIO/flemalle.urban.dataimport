# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.agorawin.importer import AgorawinDataImporter
from flemalle.urban.dataimport.interfaces import IFlemalleDataImporter


class FlemalleDataImporter(AgorawinDataImporter):
    """ """

    implements(IFlemalleDataImporter)
