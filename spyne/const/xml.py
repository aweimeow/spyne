
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

"""The ``spyne.const.xml`` module contains various XML-related constants like
namespace prefixes, namespace values and schema uris.
"""

NS_XML = 'http://www.w3.org/XML/1998/namespace'
NS_XSD = 'http://www.w3.org/2001/XMLSchema'
NS_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
NS_WSA = 'http://schemas.xmlsoap.org/ws/2003/03/addressing'
NS_XOP = 'http://www.w3.org/2004/08/xop/include'
NS_XHTML = 'http://www.w3.org/1999/xhtml'
NS_PLINK = 'http://schemas.xmlsoap.org/ws/2003/05/partner-link/'
NS_SOAP11_ENC = 'http://schemas.xmlsoap.org/soap/encoding/'
NS_SOAP11_ENV = 'http://schemas.xmlsoap.org/soap/envelope/'
NS_SOAP12_ENC = 'http://www.w3.org/2003/05/soap-encoding'
NS_SOAP12_ENV = 'http://www.w3.org/2003/05/soap-envelope'

NS_WSDL11 = 'http://schemas.xmlsoap.org/wsdl/'
NS_WSDL11_SOAP = 'http://schemas.xmlsoap.org/wsdl/soap/'
NS_WSDL11_SOAP12 = 'http://schemas.xmlsoap.org/wsdl/soap12/'
NS_WSDL11_HTTP = 'http://schemas.xmlsoap.org/wsdl/http/'

NSMAP = {
    'xml': NS_XML,
    'xs': NS_XSD,
    'xsi': NS_XSI,
    'plink': NS_PLINK,
    'wsdlsoap11': NS_WSDL11_SOAP,
    'wsdlsoap12': NS_WSDL11_SOAP12,
    'wsdl': NS_WSDL11,
    'soapenc': NS_SOAP11_ENC,
    'soapenv': NS_SOAP11_ENV,
    'soap12env': NS_SOAP12_ENV,
    'soap12enc': NS_SOAP12_ENC,
    'wsa': NS_WSA,
    'xop': NS_XOP,
    'http': NS_WSDL11_HTTP,
}

PREFMAP = None
def _regen_prefmap():
    global PREFMAP
    PREFMAP = dict([(b, a) for a, b in NSMAP.items()])
_regen_prefmap()

schema_location = {
    NS_XSD: 'http://www.w3.org/2001/XMLSchema.xsd',
}


class DEFAULT_NS(object): pass


def get_binding_ns(protocol_type):
    "Returns the wsdl binding namespace based on the protocol type"
    if 'soap12' in protocol_type:
        return WSDL11_SOAP12
    elif 'http' in protocol_type:
        return WSDL11_HTTP
    else:
        # Bind to Soap1.1 namespace by default for backwards compatibility
        return WSDL11_SOAP


def Tnswrap(ns):
    return lambda s: "{%s}%s" % (ns, s)


XML = Tnswrap(NS_XML)
XSD = Tnswrap(NS_XSD)
XSI = Tnswrap(NS_XSI)
WSA = Tnswrap(NS_WSA)
XOP = Tnswrap(NS_XOP)
XHTML = Tnswrap(NS_XHTML)
PLINK = Tnswrap(NS_PLINK)
SOAP11_ENC = Tnswrap(NS_SOAP11_ENC)
SOAP11_ENV = Tnswrap(NS_SOAP11_ENV)
SOAP12_ENC = Tnswrap(NS_SOAP12_ENC)
SOAP12_ENV = Tnswrap(NS_SOAP12_ENV)
WSDL11 = Tnswrap(NS_WSDL11)
WSDL11_SOAP = Tnswrap(NS_WSDL11_SOAP)
WSDL11_SOAP12 = Tnswrap(NS_WSDL11_SOAP12)
WSDL11_HTTP = Tnswrap(NS_WSDL11_HTTP)

# names starting with underscore need () around to be used as proper regexps
_PATT_BASE_CHAR = \
    u"[\u0041-\u005A]|[\u0061-\u007A]|[\u00C0-\u00D6]|[\u00D8-\u00F6]" \
    u"|[\u00F8-\u00FF]|[\u0100-\u0131]|[\u0134-\u013E]|[\u0141-\u0148]" \
    u"|[\u014A-\u017E]|[\u0180-\u01C3]|[\u01CD-\u01F0]|[\u01F4-\u01F5]" \
    u"|[\u01FA-\u0217]|[\u0250-\u02A8]|[\u02BB-\u02C1]|\u0386|[\u0388-\u038A]" \
    u"|\u038C|[\u038E-\u03A1]|[\u03A3-\u03CE]|[\u03D0-\u03D6]" \
    u"|\u03DA|\u03DC|\u03DE|\u03E0|[\u03E2-\u03F3]|[\u0401-\u040C]" \
    u"|[\u040E-\u044F]|[\u0451-\u045C]|[\u045E-\u0481]|[\u0490-\u04C4]" \
    u"|[\u04C7-\u04C8]|[\u04CB-\u04CC]|[\u04D0-\u04EB]|[\u04EE-\u04F5]" \
    u"|[\u04F8-\u04F9]|[\u0531-\u0556]|\u0559|[\u0561-\u0586]|[\u05D0-\u05EA]" \
    u"|[\u05F0-\u05F2]|[\u0621-\u063A]|[\u0641-\u064A]|[\u0671-\u06B7]" \
    u"|[\u06BA-\u06BE]|[\u06C0-\u06CE]|[\u06D0-\u06D3]|\u06D5|[\u06E5-\u06E6]" \
    u"|[\u0905-\u0939]|\u093D|[\u0958-\u0961]|[\u0985-\u098C]|[\u098F-\u0990]" \
    u"|[\u0993-\u09A8]|[\u09AA-\u09B0]|\u09B2|[\u09B6-\u09B9]|[\u09DC-\u09DD]" \
    u"|[\u09DF-\u09E1]|[\u09F0-\u09F1]|[\u0A05-\u0A0A]|[\u0A0F-\u0A10]" \
    u"|[\u0A13-\u0A28]|[\u0A2A-\u0A30]|[\u0A32-\u0A33]|[\u0A35-\u0A36]" \
    u"|[\u0A38-\u0A39]|[\u0A59-\u0A5C]|\u0A5E|[\u0A72-\u0A74]|[\u0A85-\u0A8B]" \
    u"|\u0A8D|[\u0A8F-\u0A91]|[\u0A93-\u0AA8]|[\u0AAA-\u0AB0]|[\u0AB2-\u0AB3]" \
    u"|[\u0AB5-\u0AB9]|\u0ABD|\u0AE0|[\u0B05-\u0B0C]|[\u0B0F-\u0B10]" \
    u"|[\u0B13-\u0B28]|[\u0B2A-\u0B30]|[\u0B32-\u0B33]|[\u0B36-\u0B39]|\u0B3D" \
    u"|[\u0B5C-\u0B5D]|[\u0B5F-\u0B61]|[\u0B85-\u0B8A]|[\u0B8E-\u0B90]" \
    u"|[\u0B92-\u0B95]|[\u0B99-\u0B9A]|\u0B9C|[\u0B9E-\u0B9F]|[\u0BA3-\u0BA4]" \
    u"|[\u0BA8-\u0BAA]|[\u0BAE-\u0BB5]|[\u0BB7-\u0BB9]|[\u0C05-\u0C0C]" \
    u"|[\u0C0E-\u0C10]|[\u0C12-\u0C28]|[\u0C2A-\u0C33]|[\u0C35-\u0C39]" \
    u"|[\u0C60-\u0C61]|[\u0C85-\u0C8C]|[\u0C8E-\u0C90]|[\u0C92-\u0CA8]" \
    u"|[\u0CAA-\u0CB3]|[\u0CB5-\u0CB9]|\u0CDE|[\u0CE0-\u0CE1]|[\u0D05-\u0D0C]" \
    u"|[\u0D0E-\u0D10]|[\u0D12-\u0D28]|[\u0D2A-\u0D39]|[\u0D60-\u0D61]" \
    u"|[\u0E01-\u0E2E]|\u0E30|[\u0E32-\u0E33]|[\u0E40-\u0E45]|[\u0E81-\u0E82]" \
    u"|\u0E84|[\u0E87-\u0E88]|\u0E8A|\u0E8D|[\u0E94-\u0E97]|[\u0E99-\u0E9F]" \
    u"|[\u0EA1-\u0EA3]|\u0EA5|\u0EA7|[\u0EAA-\u0EAB]|[\u0EAD-\u0EAE]|\u0EB0" \
    u"|[\u0EB2-\u0EB3]|\u0EBD|[\u0EC0-\u0EC4]|[\u0F40-\u0F47]|[\u0F49-\u0F69]" \
    u"|[\u10A0-\u10C5]|[\u10D0-\u10F6]|\u1100|[\u1102-\u1103]|[\u1105-\u1107]" \
    u"|\u1109|[\u110B-\u110C]|[\u110E-\u1112]|\u113C|\u113E|\u1140|\u114C" \
    u"|\u114E|\u1150|[\u1154-\u1155]|\u1159|[\u115F-\u1161]|\u1163|\u1165" \
    u"|\u1167|\u1169|[\u116D-\u116E]|[\u1172-\u1173]|\u1175|\u119E|\u11A8" \
    u"|\u11AB|[\u11AE-\u11AF]|[\u11B7-\u11B8]|\u11BA|[\u11BC-\u11C2]|\u11EB" \
    u"|\u11F0|\u11F9|[\u1E00-\u1E9B]|[\u1EA0-\u1EF9]|[\u1F00-\u1F15]" \
    u"|[\u1F18-\u1F1D]|[\u1F20-\u1F45]|[\u1F48-\u1F4D]|[\u1F50-\u1F57]|\u1F59" \
    u"|\u1F5B|\u1F5D|[\u1F5F-\u1F7D]|[\u1F80-\u1FB4]|[\u1FB6-\u1FBC]|\u1FBE" \
    u"|[\u1FC2-\u1FC4]|[\u1FC6-\u1FCC]|[\u1FD0-\u1FD3]|[\u1FD6-\u1FDB]" \
    u"|[\u1FE0-\u1FEC]|[\u1FF2-\u1FF4]|[\u1FF6-\u1FFC]|\u2126|[\u212A-\u212B]" \
    u"|\u212E|[\u2180-\u2182]|[\u3041-\u3094]|[\u30A1-\u30FA]|[\u3105-\u312C]" \
    u"|[\uAC00-\uD7A3]"

_PATT_IDEOGRAPHIC = u"[\u4E00-\u9FA5]|\u3007|[\u3021-\u3029]"

_PATT_COMBINING_CHAR = u"[\u0300-\u0345]|[\u0360-\u0361]|[\u0483-\u0486]" \
    u"|[\u0591-\u05A1]|[\u05A3-\u05B9]|[\u05BB-\u05BD]|\u05BF|[\u05C1-\u05C2]" \
    u"|\u05C4|[\u064B-\u0652]|\u0670|[\u06D6-\u06DC]|[\u06DD-\u06DF]" \
    u"|[\u06E0-\u06E4]|[\u06E7-\u06E8]|[\u06EA-\u06ED]|[\u0901-\u0903]|\u093C" \
    u"|[\u093E-\u094C]|\u094D|[\u0951-\u0954]|[\u0962-\u0963]|[\u0981-\u0983]" \
    u"|\u09BC|\u09BE|\u09BF|[\u09C0-\u09C4]|[\u09C7-\u09C8]|[\u09CB-\u09CD]" \
    u"|\u09D7|[\u09E2-\u09E3]|\u0A02|\u0A3C|\u0A3E|\u0A3F|[\u0A40-\u0A42]" \
    u"|[\u0A47-\u0A48]|[\u0A4B-\u0A4D]|[\u0A70-\u0A71]|[\u0A81-\u0A83]|\u0ABC" \
    u"|[\u0ABE-\u0AC5]|[\u0AC7-\u0AC9]|[\u0ACB-\u0ACD]|[\u0B01-\u0B03]|\u0B3C" \
    u"|[\u0B3E-\u0B43]|[\u0B47-\u0B48]|[\u0B4B-\u0B4D]|[\u0B56-\u0B57]" \
    u"|[\u0B82-\u0B83]|[\u0BBE-\u0BC2]|[\u0BC6-\u0BC8]|[\u0BCA-\u0BCD]|\u0BD7" \
    u"|[\u0C01-\u0C03]|[\u0C3E-\u0C44]|[\u0C46-\u0C48]|[\u0C4A-\u0C4D]" \
    u"|[\u0C55-\u0C56]|[\u0C82-\u0C83]|[\u0CBE-\u0CC4]|[\u0CC6-\u0CC8]" \
    u"|[\u0CCA-\u0CCD]|[\u0CD5-\u0CD6]|[\u0D02-\u0D03]|[\u0D3E-\u0D43]" \
    u"|[\u0D46-\u0D48]|[\u0D4A-\u0D4D]|\u0D57|\u0E31|[\u0E34-\u0E3A]" \
    u"|[\u0E47-\u0E4E]|\u0EB1|[\u0EB4-\u0EB9]|[\u0EBB-\u0EBC]|[\u0EC8-\u0ECD]" \
    u"|[\u0F18-\u0F19]|\u0F35|\u0F37|\u0F39|\u0F3E|\u0F3F|[\u0F71-\u0F84]" \
    u"|[\u0F86-\u0F8B]|[\u0F90-\u0F95]|\u0F97|[\u0F99-\u0FAD]|[\u0FB1-\u0FB7]" \
    u"|\u0FB9|[\u20D0-\u20DC]|\u20E1|[\u302A-\u302F]|\u3099|\u309A"

_PATT_DIGIT = u"[\u0030-\u0039]|[\u0660-\u0669]|[\u06F0-\u06F9]|[\u0966-\u096F]" \
    u"|[\u09E6-\u09EF]|[\u0A66-\u0A6F]|[\u0AE6-\u0AEF]|[\u0B66-\u0B6F]" \
    u"|[\u0BE7-\u0BEF]|[\u0C66-\u0C6F]|[\u0CE6-\u0CEF]|[\u0D66-\u0D6F]" \
    u"|[\u0E50-\u0E59]|[\u0ED0-\u0ED9]|[\u0F20-\u0F29]"

_PATT_EXTENDER = u"\u00B7|\u02D0|\u02D1|\u0387|\u0640|\u0E46|\u0EC6|\u3005" \
    u"|[\u3031-\u3035]|[\u309D-\u309E]|[\u30FC-\u30FE]"


PATT_LETTER = u"(%s)" % u'|'.join([_PATT_BASE_CHAR, _PATT_IDEOGRAPHIC])

PATT_NAMECHAR = u"(%s)" % u'|'.join([PATT_LETTER, _PATT_DIGIT,
                  u'.', u'-', u'_', u':', _PATT_COMBINING_CHAR, _PATT_EXTENDER])

PATT_NAME = u"(%s)(%s)+" % (u'|'.join([PATT_LETTER, u'_', u':']),
                                                       u"(%s)*" % PATT_NAMECHAR)

PATT_NMTOKEN = u"(%s)+" % PATT_NAMECHAR
