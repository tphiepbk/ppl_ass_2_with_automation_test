# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u01bf\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\7\2B\n\2\f\2\16\2E\13\2\3\2\7\2H")
        buf.write("\n\2\f\2\16\2K\13\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3S\n\3\3")
        buf.write("\3\3\3\3\3\5\3X\n\3\7\3Z\n\3\f\3\16\3]\13\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4h\n\4\5\4j\n\4\3\5\3\5\3")
        buf.write("\5\3\5\6\5p\n\5\r\5\16\5q\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("z\n\5\5\5|\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0084\n\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c\n\6\7\6\u008e\n\6\f\6")
        buf.write("\16\6\u0091\13\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\u0099\n\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\b\u00a2\n\b\f\b\16\b\u00a5")
        buf.write("\13\b\3\t\3\t\3\t\3\t\7\t\u00ab\n\t\f\t\16\t\u00ae\13")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00bf\n\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00ca\n\f\f\f\16\f\u00cd\13\f\3\f")
        buf.write("\3\f\5\f\u00d1\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\7\20\u00f5\n\20\f\20\16\20\u00f8\13\20\3\20\7\20")
        buf.write("\u00fb\n\20\f\20\16\20\u00fe\13\20\3\21\3\21\5\21\u0102")
        buf.write("\n\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\5\24\u0110\n\24\3\24\3\24\3\25\3\25\3\25\5")
        buf.write("\25\u0117\n\25\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u011f")
        buf.write("\n\26\3\26\3\26\3\27\3\27\3\27\7\27\u0126\n\27\f\27\16")
        buf.write("\27\u0129\13\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0131")
        buf.write("\n\30\3\30\3\30\3\31\3\31\3\31\3\31\6\31\u0139\n\31\r")
        buf.write("\31\16\31\u013a\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u016a\n\32\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\7\33\u0175\n\33\f\33\16\33")
        buf.write("\u0178\13\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0189\n\34\f\34")
        buf.write("\16\34\u018c\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\7\35\u01a0\n\35\f\35\16\35\u01a3\13\35\3\36\3\36\3\36")
        buf.write("\5\36\u01a8\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u01af\n")
        buf.write("\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01bd\n \3")
        buf.write(" \2\5\64\668!\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>\2\2\2\u01f1\2C\3\2\2\2\4N\3\2")
        buf.write("\2\2\6`\3\2\2\2\bk\3\2\2\2\n}\3\2\2\2\f\u0094\3\2\2\2")
        buf.write("\16\u009c\3\2\2\2\20\u00a6\3\2\2\2\22\u00af\3\2\2\2\24")
        buf.write("\u00be\3\2\2\2\26\u00c0\3\2\2\2\30\u00d5\3\2\2\2\32\u00e5")
        buf.write("\3\2\2\2\34\u00ec\3\2\2\2\36\u00f6\3\2\2\2 \u0101\3\2")
        buf.write("\2\2\"\u0107\3\2\2\2$\u010a\3\2\2\2&\u010d\3\2\2\2(\u0113")
        buf.write("\3\2\2\2*\u011b\3\2\2\2,\u0122\3\2\2\2.\u0130\3\2\2\2")
        buf.write("\60\u0138\3\2\2\2\62\u0169\3\2\2\2\64\u016b\3\2\2\2\66")
        buf.write("\u0179\3\2\2\28\u018d\3\2\2\2:\u01a7\3\2\2\2<\u01ae\3")
        buf.write("\2\2\2>\u01bc\3\2\2\2@B\5\4\3\2A@\3\2\2\2BE\3\2\2\2CA")
        buf.write("\3\2\2\2CD\3\2\2\2DI\3\2\2\2EC\3\2\2\2FH\5\f\7\2GF\3\2")
        buf.write("\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2")
        buf.write("LM\7\2\2\3M\3\3\2\2\2NO\7\24\2\2OR\7\30\2\2PS\5\6\4\2")
        buf.write("QS\5\b\5\2RP\3\2\2\2RQ\3\2\2\2S[\3\2\2\2TW\7\32\2\2UX")
        buf.write("\5\6\4\2VX\5\b\5\2WU\3\2\2\2WV\3\2\2\2XZ\3\2\2\2YT\3\2")
        buf.write("\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2][\3\2\2")
        buf.write("\2^_\7\27\2\2_\5\3\2\2\2`i\7\3\2\2ag\7*\2\2bh\79\2\2c")
        buf.write("h\7;\2\2dh\7<\2\2eh\7=\2\2fh\5\n\6\2gb\3\2\2\2gc\3\2\2")
        buf.write("\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2hj\3\2\2\2ia\3\2\2\2i")
        buf.write("j\3\2\2\2j\7\3\2\2\2ko\7\3\2\2lm\7\35\2\2mn\79\2\2np\7")
        buf.write("\36\2\2ol\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2\2r{\3\2")
        buf.write("\2\2sy\7*\2\2tz\5\n\6\2uz\7;\2\2vz\79\2\2wz\7=\2\2xz\7")
        buf.write("<\2\2yt\3\2\2\2yu\3\2\2\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2")
        buf.write("\2z|\3\2\2\2{s\3\2\2\2{|\3\2\2\2|\t\3\2\2\2}\u0083\7\37")
        buf.write("\2\2~\u0084\79\2\2\177\u0084\7;\2\2\u0080\u0084\7<\2\2")
        buf.write("\u0081\u0084\7=\2\2\u0082\u0084\5\n\6\2\u0083~\3\2\2\2")
        buf.write("\u0083\177\3\2\2\2\u0083\u0080\3\2\2\2\u0083\u0081\3\2")
        buf.write("\2\2\u0083\u0082\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u008f")
        buf.write("\3\2\2\2\u0085\u008b\7\32\2\2\u0086\u008c\79\2\2\u0087")
        buf.write("\u008c\7=\2\2\u0088\u008c\7<\2\2\u0089\u008c\7;\2\2\u008a")
        buf.write("\u008c\5\n\6\2\u008b\u0086\3\2\2\2\u008b\u0087\3\2\2\2")
        buf.write("\u008b\u0088\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008a\3")
        buf.write("\2\2\2\u008c\u008e\3\2\2\2\u008d\u0085\3\2\2\2\u008e\u0091")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090")
        buf.write("\u0092\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7 \2\2")
        buf.write("\u0093\13\3\2\2\2\u0094\u0095\7\17\2\2\u0095\u0096\7\30")
        buf.write("\2\2\u0096\u0098\7\3\2\2\u0097\u0099\5\16\b\2\u0098\u0097")
        buf.write("\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\5\22\n\2\u009b\r\3\2\2\2\u009c\u009d\7\21\2\2\u009d")
        buf.write("\u009e\7\30\2\2\u009e\u00a3\5\20\t\2\u009f\u00a0\7\32")
        buf.write("\2\2\u00a0\u00a2\5\20\t\2\u00a1\u009f\3\2\2\2\u00a2\u00a5")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\17\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00ac\7\3\2\2\u00a7")
        buf.write("\u00a8\7\35\2\2\u00a8\u00a9\79\2\2\u00a9\u00ab\7\36\2")
        buf.write("\2\u00aa\u00a7\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\21\3\2\2\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00af\u00b0\7\4\2\2\u00b0\u00b1\7\30\2\2\u00b1")
        buf.write("\u00b2\5\36\20\2\u00b2\u00b3\7\n\2\2\u00b3\u00b4\7\31")
        buf.write("\2\2\u00b4\23\3\2\2\2\u00b5\u00bf\5 \21\2\u00b6\u00bf")
        buf.write("\5(\25\2\u00b7\u00bf\5\26\f\2\u00b8\u00bf\5\30\r\2\u00b9")
        buf.write("\u00bf\5\32\16\2\u00ba\u00bf\5\34\17\2\u00bb\u00bf\5&")
        buf.write("\24\2\u00bc\u00bf\5\"\22\2\u00bd\u00bf\5$\23\2\u00be\u00b5")
        buf.write("\3\2\2\2\u00be\u00b6\3\2\2\2\u00be\u00b7\3\2\2\2\u00be")
        buf.write("\u00b8\3\2\2\2\u00be\u00b9\3\2\2\2\u00be\u00ba\3\2\2\2")
        buf.write("\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3")
        buf.write("\2\2\2\u00bf\25\3\2\2\2\u00c0\u00c1\7\20\2\2\u00c1\u00c2")
        buf.write("\5\62\32\2\u00c2\u00c3\7\23\2\2\u00c3\u00cb\5\36\20\2")
        buf.write("\u00c4\u00c5\7\t\2\2\u00c5\u00c6\5\62\32\2\u00c6\u00c7")
        buf.write("\7\23\2\2\u00c7\u00c8\5\36\20\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c4\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00d0\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00cf\7\b\2\2\u00cf\u00d1\5\36\20\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d3\7\13\2\2\u00d3\u00d4\7\31\2\2\u00d4\27\3")
        buf.write("\2\2\2\u00d5\u00d6\7\16\2\2\u00d6\u00d7\7\33\2\2\u00d7")
        buf.write("\u00d8\7\3\2\2\u00d8\u00d9\7*\2\2\u00d9\u00da\5\62\32")
        buf.write("\2\u00da\u00db\7\32\2\2\u00db\u00dc\5\62\32\2\u00dc\u00dd")
        buf.write("\7\32\2\2\u00dd\u00de\5\62\32\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e0\7\34\2\2\u00e0\u00e1\7\7\2\2\u00e1\u00e2\5\36\20")
        buf.write("\2\u00e2\u00e3\7\f\2\2\u00e3\u00e4\7\31\2\2\u00e4\31\3")
        buf.write("\2\2\2\u00e5\u00e6\7\25\2\2\u00e6\u00e7\5\62\32\2\u00e7")
        buf.write("\u00e8\7\7\2\2\u00e8\u00e9\5\36\20\2\u00e9\u00ea\7\r\2")
        buf.write("\2\u00ea\u00eb\7\31\2\2\u00eb\33\3\2\2\2\u00ec\u00ed\7")
        buf.write("\7\2\2\u00ed\u00ee\5\36\20\2\u00ee\u00ef\7\25\2\2\u00ef")
        buf.write("\u00f0\5\62\32\2\u00f0\u00f1\7\26\2\2\u00f1\u00f2\7\31")
        buf.write("\2\2\u00f2\35\3\2\2\2\u00f3\u00f5\5\4\3\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7\u00fc\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f9\u00fb\5\24\13\2\u00fa\u00f9\3\2\2\2\u00fb\u00fe")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\37\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0102\7\3\2\2\u0100")
        buf.write("\u0102\5.\30\2\u0101\u00ff\3\2\2\2\u0101\u0100\3\2\2\2")
        buf.write("\u0102\u0103\3\2\2\2\u0103\u0104\7*\2\2\u0104\u0105\5")
        buf.write("\62\32\2\u0105\u0106\7\27\2\2\u0106!\3\2\2\2\u0107\u0108")
        buf.write("\7\5\2\2\u0108\u0109\7\27\2\2\u0109#\3\2\2\2\u010a\u010b")
        buf.write("\7\6\2\2\u010b\u010c\7\27\2\2\u010c%\3\2\2\2\u010d\u010f")
        buf.write("\7\22\2\2\u010e\u0110\5\62\32\2\u010f\u010e\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\7\27\2")
        buf.write("\2\u0112\'\3\2\2\2\u0113\u0114\7\3\2\2\u0114\u0116\7\33")
        buf.write("\2\2\u0115\u0117\5,\27\2\u0116\u0115\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\7\34\2\2\u0119")
        buf.write("\u011a\7\27\2\2\u011a)\3\2\2\2\u011b\u011c\7\3\2\2\u011c")
        buf.write("\u011e\7\33\2\2\u011d\u011f\5,\27\2\u011e\u011d\3\2\2")
        buf.write("\2\u011e\u011f\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0121")
        buf.write("\7\34\2\2\u0121+\3\2\2\2\u0122\u0127\5\62\32\2\u0123\u0124")
        buf.write("\7\32\2\2\u0124\u0126\5\62\32\2\u0125\u0123\3\2\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128-\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7\33\2")
        buf.write("\2\u012b\u012c\5\62\32\2\u012c\u012d\7\34\2\2\u012d\u0131")
        buf.write("\3\2\2\2\u012e\u0131\7\3\2\2\u012f\u0131\5*\26\2\u0130")
        buf.write("\u012a\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0133\5\60\31\2\u0133/\3\2")
        buf.write("\2\2\u0134\u0135\7\35\2\2\u0135\u0136\5\62\32\2\u0136")
        buf.write("\u0137\7\36\2\2\u0137\u0139\3\2\2\2\u0138\u0134\3\2\2")
        buf.write("\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b\61\3\2\2\2\u013c\u013d\5\64\33\2\u013d")
        buf.write("\u013e\7.\2\2\u013e\u013f\5\64\33\2\u013f\u016a\3\2\2")
        buf.write("\2\u0140\u0141\5\64\33\2\u0141\u0142\7/\2\2\u0142\u0143")
        buf.write("\5\64\33\2\u0143\u016a\3\2\2\2\u0144\u0145\5\64\33\2\u0145")
        buf.write("\u0146\7\60\2\2\u0146\u0147\5\64\33\2\u0147\u016a\3\2")
        buf.write("\2\2\u0148\u0149\5\64\33\2\u0149\u014a\7\61\2\2\u014a")
        buf.write("\u014b\5\64\33\2\u014b\u016a\3\2\2\2\u014c\u014d\5\64")
        buf.write("\33\2\u014d\u014e\7\63\2\2\u014e\u014f\5\64\33\2\u014f")
        buf.write("\u016a\3\2\2\2\u0150\u0151\5\64\33\2\u0151\u0152\7\62")
        buf.write("\2\2\u0152\u0153\5\64\33\2\u0153\u016a\3\2\2\2\u0154\u0155")
        buf.write("\5\64\33\2\u0155\u0156\7\64\2\2\u0156\u0157\5\64\33\2")
        buf.write("\u0157\u016a\3\2\2\2\u0158\u0159\5\64\33\2\u0159\u015a")
        buf.write("\7\65\2\2\u015a\u015b\5\64\33\2\u015b\u016a\3\2\2\2\u015c")
        buf.write("\u015d\5\64\33\2\u015d\u015e\7\66\2\2\u015e\u015f\5\64")
        buf.write("\33\2\u015f\u016a\3\2\2\2\u0160\u0161\5\64\33\2\u0161")
        buf.write("\u0162\7\67\2\2\u0162\u0163\5\64\33\2\u0163\u016a\3\2")
        buf.write("\2\2\u0164\u0165\5\64\33\2\u0165\u0166\78\2\2\u0166\u0167")
        buf.write("\5\64\33\2\u0167\u016a\3\2\2\2\u0168\u016a\5\64\33\2\u0169")
        buf.write("\u013c\3\2\2\2\u0169\u0140\3\2\2\2\u0169\u0144\3\2\2\2")
        buf.write("\u0169\u0148\3\2\2\2\u0169\u014c\3\2\2\2\u0169\u0150\3")
        buf.write("\2\2\2\u0169\u0154\3\2\2\2\u0169\u0158\3\2\2\2\u0169\u015c")
        buf.write("\3\2\2\2\u0169\u0160\3\2\2\2\u0169\u0164\3\2\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\63\3\2\2\2\u016b\u016c\b\33\1\2\u016c")
        buf.write("\u016d\5\66\34\2\u016d\u0176\3\2\2\2\u016e\u016f\f\5\2")
        buf.write("\2\u016f\u0170\7,\2\2\u0170\u0175\5\66\34\2\u0171\u0172")
        buf.write("\f\4\2\2\u0172\u0173\7-\2\2\u0173\u0175\5\66\34\2\u0174")
        buf.write("\u016e\3\2\2\2\u0174\u0171\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177\65\3\2")
        buf.write("\2\2\u0178\u0176\3\2\2\2\u0179\u017a\b\34\1\2\u017a\u017b")
        buf.write("\58\35\2\u017b\u018a\3\2\2\2\u017c\u017d\f\7\2\2\u017d")
        buf.write("\u017e\7!\2\2\u017e\u0189\58\35\2\u017f\u0180\f\6\2\2")
        buf.write("\u0180\u0181\7\"\2\2\u0181\u0189\58\35\2\u0182\u0183\f")
        buf.write("\5\2\2\u0183\u0184\7$\2\2\u0184\u0189\58\35\2\u0185\u0186")
        buf.write("\f\4\2\2\u0186\u0187\7#\2\2\u0187\u0189\58\35\2\u0188")
        buf.write("\u017c\3\2\2\2\u0188\u017f\3\2\2\2\u0188\u0182\3\2\2\2")
        buf.write("\u0188\u0185\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018b\67\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018d\u018e\b\35\1\2\u018e\u018f\5:\36\2\u018f")
        buf.write("\u01a1\3\2\2\2\u0190\u0191\f\b\2\2\u0191\u0192\7&\2\2")
        buf.write("\u0192\u01a0\5:\36\2\u0193\u0194\f\7\2\2\u0194\u0195\7")
        buf.write("%\2\2\u0195\u01a0\5:\36\2\u0196\u0197\f\6\2\2\u0197\u0198")
        buf.write("\7(\2\2\u0198\u01a0\5:\36\2\u0199\u019a\f\5\2\2\u019a")
        buf.write("\u019b\7\'\2\2\u019b\u01a0\5:\36\2\u019c\u019d\f\4\2\2")
        buf.write("\u019d\u019e\7)\2\2\u019e\u01a0\5:\36\2\u019f\u0190\3")
        buf.write("\2\2\2\u019f\u0193\3\2\2\2\u019f\u0196\3\2\2\2\u019f\u0199")
        buf.write("\3\2\2\2\u019f\u019c\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a29\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\7+\2\2\u01a5\u01a8\5:\36\2")
        buf.write("\u01a6\u01a8\5<\37\2\u01a7\u01a4\3\2\2\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a8;\3\2\2\2\u01a9\u01aa\7$\2\2\u01aa\u01af\5")
        buf.write("<\37\2\u01ab\u01ac\7#\2\2\u01ac\u01af\5<\37\2\u01ad\u01af")
        buf.write("\5> \2\u01ae\u01a9\3\2\2\2\u01ae\u01ab\3\2\2\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01af=\3\2\2\2\u01b0\u01bd\7\3\2\2\u01b1\u01bd")
        buf.write("\79\2\2\u01b2\u01bd\7;\2\2\u01b3\u01bd\5*\26\2\u01b4\u01bd")
        buf.write("\5.\30\2\u01b5\u01bd\7=\2\2\u01b6\u01bd\7<\2\2\u01b7\u01bd")
        buf.write("\5\n\6\2\u01b8\u01b9\7\33\2\2\u01b9\u01ba\5\62\32\2\u01ba")
        buf.write("\u01bb\7\34\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01b0\3\2\2")
        buf.write("\2\u01bc\u01b1\3\2\2\2\u01bc\u01b2\3\2\2\2\u01bc\u01b3")
        buf.write("\3\2\2\2\u01bc\u01b4\3\2\2\2\u01bc\u01b5\3\2\2\2\u01bc")
        buf.write("\u01b6\3\2\2\2\u01bc\u01b7\3\2\2\2\u01bc\u01b8\3\2\2\2")
        buf.write("\u01bd?\3\2\2\2(CIRW[giqy{\u0083\u008b\u008f\u0098\u00a3")
        buf.write("\u00ac\u00be\u00cb\u00d0\u00f6\u00fc\u0101\u010f\u0116")
        buf.write("\u011e\u0127\u0130\u013a\u0169\u0174\u0176\u0188\u018a")
        buf.write("\u019f\u01a1\u01a7\u01ae\u01bc")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'EndDo'", "';'", "':'", "'.'", "','", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "'+'", "<INVALID>", "'-'", 
                     "<INVALID>", "'*'", "<INVALID>", "'\\'", "<INVALID>", 
                     "'%'", "'='", "'!'", "'&&'", "'||'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'=/='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'0'", "<INVALID>", "<INVALID>", "<INVALID>", "'True'", 
                     "'False'" ]

    symbolicNames = [ "<INVALID>", "ID", "BODY", "BREAK", "CONTINUE", "DO", 
                      "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
                      "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", 
                      "VAR", "WHILE", "ENDDO", "SEMI", "COLON", "DOT", "COMMA", 
                      "LP", "RP", "LSB", "RSB", "LB", "RB", "ADD_INT", "ADD_FLOAT", 
                      "SUB_INT", "SUB_FLOAT", "MUL_INT", "MUL_FLOAT", "DIV_INT", 
                      "DIV_FLOAT", "MOD", "ASSIGN", "NOT", "AND", "OR", 
                      "EQUAL", "NOTEQUAL_INT", "LT_INT", "GT_INT", "LTE_INT", 
                      "GTE_INT", "NOTEQUAL_FLOAT", "LT_FLOAT", "GT_FLOAT", 
                      "LTE_FLOAT", "GTE_FLOAT", "INT_LIT", "ZERO_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "BOOL_LIT", "TRUE", "FALSE", "COMMENT", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_declaration_part = 1
    RULE_single_var_list = 2
    RULE_array_list = 3
    RULE_array_lit = 4
    RULE_func_declaration_part = 5
    RULE_param_list = 6
    RULE_param_element = 7
    RULE_func_body = 8
    RULE_statement_in_function = 9
    RULE_if_statement_in_function = 10
    RULE_for_statement_in_function = 11
    RULE_while_statement_in_function = 12
    RULE_do_while_statement_in_function = 13
    RULE_var_decl_and_statement = 14
    RULE_assignment = 15
    RULE_break_statement = 16
    RULE_continue_statement = 17
    RULE_return_statement = 18
    RULE_function_call_statement = 19
    RULE_function_call = 20
    RULE_argument_list = 21
    RULE_element_expression = 22
    RULE_index_operators = 23
    RULE_exp = 24
    RULE_exp1 = 25
    RULE_exp2 = 26
    RULE_exp3 = 27
    RULE_exp4 = 28
    RULE_exp5 = 29
    RULE_operand = 30

    ruleNames =  [ "program", "var_declaration_part", "single_var_list", 
                   "array_list", "array_lit", "func_declaration_part", "param_list", 
                   "param_element", "func_body", "statement_in_function", 
                   "if_statement_in_function", "for_statement_in_function", 
                   "while_statement_in_function", "do_while_statement_in_function", 
                   "var_decl_and_statement", "assignment", "break_statement", 
                   "continue_statement", "return_statement", "function_call_statement", 
                   "function_call", "argument_list", "element_expression", 
                   "index_operators", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "operand" ]

    EOF = Token.EOF
    ID=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    ENDDO=20
    SEMI=21
    COLON=22
    DOT=23
    COMMA=24
    LP=25
    RP=26
    LSB=27
    RSB=28
    LB=29
    RB=30
    ADD_INT=31
    ADD_FLOAT=32
    SUB_INT=33
    SUB_FLOAT=34
    MUL_INT=35
    MUL_FLOAT=36
    DIV_INT=37
    DIV_FLOAT=38
    MOD=39
    ASSIGN=40
    NOT=41
    AND=42
    OR=43
    EQUAL=44
    NOTEQUAL_INT=45
    LT_INT=46
    GT_INT=47
    LTE_INT=48
    GTE_INT=49
    NOTEQUAL_FLOAT=50
    LT_FLOAT=51
    GT_FLOAT=52
    LTE_FLOAT=53
    GTE_FLOAT=54
    INT_LIT=55
    ZERO_LIT=56
    FLOAT_LIT=57
    STRING_LIT=58
    BOOL_LIT=59
    TRUE=60
    FALSE=61
    COMMENT=62
    WS=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    UNTERMINATED_COMMENT=66
    ERROR_CHAR=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_declaration_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declaration_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declaration_partContext,i)


        def func_declaration_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declaration_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declaration_partContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 62
                self.var_declaration_part()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 68
                self.func_declaration_part()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declaration_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def single_var_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Single_var_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Single_var_listContext,i)


        def array_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_listContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_declaration_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration_part" ):
                return visitor.visitVar_declaration_part(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration_part(self):

        localctx = BKITParser.Var_declaration_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declaration_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(BKITParser.VAR)
            self.state = 77
            self.match(BKITParser.COLON)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 78
                self.single_var_list()
                pass

            elif la_ == 2:
                self.state = 79
                self.array_list()
                pass


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 82
                self.match(BKITParser.COMMA)
                self.state = 85
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 83
                    self.single_var_list()
                    pass

                elif la_ == 2:
                    self.state = 84
                    self.array_list()
                    pass


                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_single_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_var_list" ):
                return visitor.visitSingle_var_list(self)
            else:
                return visitor.visitChildren(self)




    def single_var_list(self):

        localctx = BKITParser.Single_var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_single_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(BKITParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 95
                self.match(BKITParser.ASSIGN)
                self.state = 101
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT_LIT]:
                    self.state = 96
                    self.match(BKITParser.INT_LIT)
                    pass
                elif token in [BKITParser.FLOAT_LIT]:
                    self.state = 97
                    self.match(BKITParser.FLOAT_LIT)
                    pass
                elif token in [BKITParser.STRING_LIT]:
                    self.state = 98
                    self.match(BKITParser.STRING_LIT)
                    pass
                elif token in [BKITParser.BOOL_LIT]:
                    self.state = 99
                    self.match(BKITParser.BOOL_LIT)
                    pass
                elif token in [BKITParser.LB]:
                    self.state = 100
                    self.array_lit()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(BKITParser.ID)
            self.state = 109 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.match(BKITParser.LSB)
                self.state = 107
                self.match(BKITParser.INT_LIT)
                self.state = 108
                self.match(BKITParser.RSB)
                self.state = 111 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LSB):
                    break

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 113
                self.match(BKITParser.ASSIGN)
                self.state = 119
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LB]:
                    self.state = 114
                    self.array_lit()
                    pass
                elif token in [BKITParser.FLOAT_LIT]:
                    self.state = 115
                    self.match(BKITParser.FLOAT_LIT)
                    pass
                elif token in [BKITParser.INT_LIT]:
                    self.state = 116
                    self.match(BKITParser.INT_LIT)
                    pass
                elif token in [BKITParser.BOOL_LIT]:
                    self.state = 117
                    self.match(BKITParser.BOOL_LIT)
                    pass
                elif token in [BKITParser.STRING_LIT]:
                    self.state = 118
                    self.match(BKITParser.STRING_LIT)
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def FLOAT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.FLOAT_LIT)
            else:
                return self.getToken(BKITParser.FLOAT_LIT, i)

        def STRING_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.STRING_LIT)
            else:
                return self.getToken(BKITParser.STRING_LIT, i)

        def BOOL_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.BOOL_LIT)
            else:
                return self.getToken(BKITParser.BOOL_LIT, i)

        def array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_litContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_litContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(BKITParser.LB)
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT_LIT]:
                self.state = 124
                self.match(BKITParser.INT_LIT)
                pass
            elif token in [BKITParser.FLOAT_LIT]:
                self.state = 125
                self.match(BKITParser.FLOAT_LIT)
                pass
            elif token in [BKITParser.STRING_LIT]:
                self.state = 126
                self.match(BKITParser.STRING_LIT)
                pass
            elif token in [BKITParser.BOOL_LIT]:
                self.state = 127
                self.match(BKITParser.BOOL_LIT)
                pass
            elif token in [BKITParser.LB]:
                self.state = 128
                self.array_lit()
                pass
            elif token in [BKITParser.COMMA, BKITParser.RB]:
                pass
            else:
                pass
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 131
                self.match(BKITParser.COMMA)
                self.state = 137
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT_LIT]:
                    self.state = 132
                    self.match(BKITParser.INT_LIT)
                    pass
                elif token in [BKITParser.BOOL_LIT]:
                    self.state = 133
                    self.match(BKITParser.BOOL_LIT)
                    pass
                elif token in [BKITParser.STRING_LIT]:
                    self.state = 134
                    self.match(BKITParser.STRING_LIT)
                    pass
                elif token in [BKITParser.FLOAT_LIT]:
                    self.state = 135
                    self.match(BKITParser.FLOAT_LIT)
                    pass
                elif token in [BKITParser.LB]:
                    self.state = 136
                    self.array_lit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declaration_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declaration_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declaration_part" ):
                return visitor.visitFunc_declaration_part(self)
            else:
                return visitor.visitChildren(self)




    def func_declaration_part(self):

        localctx = BKITParser.Func_declaration_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_declaration_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(BKITParser.FUNCTION)
            self.state = 147
            self.match(BKITParser.COLON)
            self.state = 148
            self.match(BKITParser.ID)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 149
                self.param_list()


            self.state = 152
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def param_element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Param_elementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Param_elementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.PARAMETER)
            self.state = 155
            self.match(BKITParser.COLON)
            self.state = 156
            self.param_element()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 157
                self.match(BKITParser.COMMA)
                self.state = 158
                self.param_element()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_element" ):
                return visitor.visitParam_element(self)
            else:
                return visitor.visitChildren(self)




    def param_element(self):

        localctx = BKITParser.Param_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKITParser.ID)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 165
                self.match(BKITParser.LSB)
                self.state = 166
                self.match(BKITParser.INT_LIT)
                self.state = 167
                self.match(BKITParser.RSB)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_decl_and_statement(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_and_statementContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(BKITParser.BODY)
            self.state = 174
            self.match(BKITParser.COLON)
            self.state = 175
            self.var_decl_and_statement()
            self.state = 176
            self.match(BKITParser.ENDBODY)
            self.state = 177
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_in_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(BKITParser.AssignmentContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(BKITParser.Function_call_statementContext,0)


        def if_statement_in_function(self):
            return self.getTypedRuleContext(BKITParser.If_statement_in_functionContext,0)


        def for_statement_in_function(self):
            return self.getTypedRuleContext(BKITParser.For_statement_in_functionContext,0)


        def while_statement_in_function(self):
            return self.getTypedRuleContext(BKITParser.While_statement_in_functionContext,0)


        def do_while_statement_in_function(self):
            return self.getTypedRuleContext(BKITParser.Do_while_statement_in_functionContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(BKITParser.Return_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(BKITParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(BKITParser.Continue_statementContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_in_function" ):
                return visitor.visitStatement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def statement_in_function(self):

        localctx = BKITParser.Statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 179
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 180
                self.function_call_statement()
                pass

            elif la_ == 3:
                self.state = 181
                self.if_statement_in_function()
                pass

            elif la_ == 4:
                self.state = 182
                self.for_statement_in_function()
                pass

            elif la_ == 5:
                self.state = 183
                self.while_statement_in_function()
                pass

            elif la_ == 6:
                self.state = 184
                self.do_while_statement_in_function()
                pass

            elif la_ == 7:
                self.state = 185
                self.return_statement()
                pass

            elif la_ == 8:
                self.state = 186
                self.break_statement()
                pass

            elif la_ == 9:
                self.state = 187
                self.continue_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statement_in_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def var_decl_and_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decl_and_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decl_and_statementContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement_in_function" ):
                return visitor.visitIf_statement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def if_statement_in_function(self):

        localctx = BKITParser.If_statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_if_statement_in_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BKITParser.IF)

            self.state = 191
            self.exp()
            self.state = 192
            self.match(BKITParser.THEN)
            self.state = 193
            self.var_decl_and_statement()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 194
                self.match(BKITParser.ELSEIF)

                self.state = 195
                self.exp()
                self.state = 196
                self.match(BKITParser.THEN)
                self.state = 197
                self.var_decl_and_statement()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 204
                self.match(BKITParser.ELSE)
                self.state = 205
                self.var_decl_and_statement()


            self.state = 208
            self.match(BKITParser.ENDIF)
            self.state = 209
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statement_in_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_decl_and_statement(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_and_statementContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement_in_function" ):
                return visitor.visitFor_statement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def for_statement_in_function(self):

        localctx = BKITParser.For_statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_statement_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BKITParser.FOR)
            self.state = 212
            self.match(BKITParser.LP)

            self.state = 213
            self.match(BKITParser.ID)
            self.state = 214
            self.match(BKITParser.ASSIGN)
            self.state = 215
            self.exp()
            self.state = 216
            self.match(BKITParser.COMMA)
            self.state = 217
            self.exp()
            self.state = 218
            self.match(BKITParser.COMMA)
            self.state = 219
            self.exp()
            self.state = 221
            self.match(BKITParser.RP)
            self.state = 222
            self.match(BKITParser.DO)
            self.state = 223
            self.var_decl_and_statement()
            self.state = 224
            self.match(BKITParser.ENDFOR)
            self.state = 225
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statement_in_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_decl_and_statement(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_and_statementContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_while_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement_in_function" ):
                return visitor.visitWhile_statement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def while_statement_in_function(self):

        localctx = BKITParser.While_statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_while_statement_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(BKITParser.WHILE)

            self.state = 228
            self.exp()
            self.state = 229
            self.match(BKITParser.DO)
            self.state = 230
            self.var_decl_and_statement()
            self.state = 231
            self.match(BKITParser.ENDWHILE)
            self.state = 232
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statement_in_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def var_decl_and_statement(self):
            return self.getTypedRuleContext(BKITParser.Var_decl_and_statementContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement_in_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement_in_function" ):
                return visitor.visitDo_while_statement_in_function(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement_in_function(self):

        localctx = BKITParser.Do_while_statement_in_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_do_while_statement_in_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.DO)
            self.state = 235
            self.var_decl_and_statement()
            self.state = 236
            self.match(BKITParser.WHILE)

            self.state = 237
            self.exp()
            self.state = 238
            self.match(BKITParser.ENDDO)
            self.state = 239
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_and_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declaration_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declaration_partContext,i)


        def statement_in_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Statement_in_functionContext)
            else:
                return self.getTypedRuleContext(BKITParser.Statement_in_functionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_and_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_and_statement" ):
                return visitor.visitVar_decl_and_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_and_statement(self):

        localctx = BKITParser.Var_decl_and_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_decl_and_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 241
                self.var_declaration_part()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 250
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 247
                    self.statement_in_function() 
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def element_expression(self):
            return self.getTypedRuleContext(BKITParser.Element_expressionContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = BKITParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.state = 254
                self.element_expression()
                pass


            self.state = 257
            self.match(BKITParser.ASSIGN)

            self.state = 258
            self.exp()
            self.state = 259
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(BKITParser.BREAK)
            self.state = 262
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(BKITParser.CONTINUE)
            self.state = 265
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.RETURN)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.SUB_INT) | (1 << BKITParser.SUB_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.BOOL_LIT))) != 0):
                self.state = 268
                self.exp()


            self.state = 271
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BKITParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = BKITParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(BKITParser.ID)
            self.state = 274
            self.match(BKITParser.LP)
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.SUB_INT) | (1 << BKITParser.SUB_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.BOOL_LIT))) != 0):
                self.state = 275
                self.argument_list()


            self.state = 278
            self.match(BKITParser.RP)
            self.state = 279
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def argument_list(self):
            return self.getTypedRuleContext(BKITParser.Argument_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(BKITParser.ID)
            self.state = 282
            self.match(BKITParser.LP)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.LP) | (1 << BKITParser.LB) | (1 << BKITParser.SUB_INT) | (1 << BKITParser.SUB_FLOAT) | (1 << BKITParser.NOT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.BOOL_LIT))) != 0):
                self.state = 283
                self.argument_list()


            self.state = 286
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_argument_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = BKITParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.exp()
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 289
                self.match(BKITParser.COMMA)
                self.state = 290
                self.exp()
                self.state = 295
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_expression" ):
                return visitor.visitElement_expression(self)
            else:
                return visitor.visitChildren(self)




    def element_expression(self):

        localctx = BKITParser.Element_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_element_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 296
                self.match(BKITParser.LP)
                self.state = 297
                self.exp()
                self.state = 298
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.state = 300
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.state = 301
                self.function_call()
                pass


            self.state = 304
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 306
                    self.match(BKITParser.LSB)
                    self.state = 307
                    self.exp()
                    self.state = 308
                    self.match(BKITParser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 312 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOTEQUAL_INT(self):
            return self.getToken(BKITParser.NOTEQUAL_INT, 0)

        def LT_INT(self):
            return self.getToken(BKITParser.LT_INT, 0)

        def GT_INT(self):
            return self.getToken(BKITParser.GT_INT, 0)

        def GTE_INT(self):
            return self.getToken(BKITParser.GTE_INT, 0)

        def LTE_INT(self):
            return self.getToken(BKITParser.LTE_INT, 0)

        def NOTEQUAL_FLOAT(self):
            return self.getToken(BKITParser.NOTEQUAL_FLOAT, 0)

        def LT_FLOAT(self):
            return self.getToken(BKITParser.LT_FLOAT, 0)

        def GT_FLOAT(self):
            return self.getToken(BKITParser.GT_FLOAT, 0)

        def LTE_FLOAT(self):
            return self.getToken(BKITParser.LTE_FLOAT, 0)

        def GTE_FLOAT(self):
            return self.getToken(BKITParser.GTE_FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.exp1(0)
                self.state = 315
                self.match(BKITParser.EQUAL)
                self.state = 316
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.exp1(0)
                self.state = 319
                self.match(BKITParser.NOTEQUAL_INT)
                self.state = 320
                self.exp1(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.exp1(0)
                self.state = 323
                self.match(BKITParser.LT_INT)
                self.state = 324
                self.exp1(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.exp1(0)
                self.state = 327
                self.match(BKITParser.GT_INT)
                self.state = 328
                self.exp1(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
                self.exp1(0)
                self.state = 331
                self.match(BKITParser.GTE_INT)
                self.state = 332
                self.exp1(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 334
                self.exp1(0)
                self.state = 335
                self.match(BKITParser.LTE_INT)
                self.state = 336
                self.exp1(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 338
                self.exp1(0)
                self.state = 339
                self.match(BKITParser.NOTEQUAL_FLOAT)
                self.state = 340
                self.exp1(0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 342
                self.exp1(0)
                self.state = 343
                self.match(BKITParser.LT_FLOAT)
                self.state = 344
                self.exp1(0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 346
                self.exp1(0)
                self.state = 347
                self.match(BKITParser.GT_FLOAT)
                self.state = 348
                self.exp1(0)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 350
                self.exp1(0)
                self.state = 351
                self.match(BKITParser.LTE_FLOAT)
                self.state = 352
                self.exp1(0)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 354
                self.exp1(0)
                self.state = 355
                self.match(BKITParser.GTE_FLOAT)
                self.state = 356
                self.exp1(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 358
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 370
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 364
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 365
                        self.match(BKITParser.AND)
                        self.state = 366
                        self.exp2(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                        self.state = 367
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 368
                        self.match(BKITParser.OR)
                        self.state = 369
                        self.exp2(0)
                        pass

             
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD_INT(self):
            return self.getToken(BKITParser.ADD_INT, 0)

        def ADD_FLOAT(self):
            return self.getToken(BKITParser.ADD_FLOAT, 0)

        def SUB_FLOAT(self):
            return self.getToken(BKITParser.SUB_FLOAT, 0)

        def SUB_INT(self):
            return self.getToken(BKITParser.SUB_INT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 392
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 390
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 378
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 379
                        self.match(BKITParser.ADD_INT)
                        self.state = 380
                        self.exp3(0)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 381
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 382
                        self.match(BKITParser.ADD_FLOAT)
                        self.state = 383
                        self.exp3(0)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 384
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 385
                        self.match(BKITParser.SUB_FLOAT)
                        self.state = 386
                        self.exp3(0)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 387
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 388
                        self.match(BKITParser.SUB_INT)
                        self.state = 389
                        self.exp3(0)
                        pass

             
                self.state = 394
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL_FLOAT(self):
            return self.getToken(BKITParser.MUL_FLOAT, 0)

        def MUL_INT(self):
            return self.getToken(BKITParser.MUL_INT, 0)

        def DIV_FLOAT(self):
            return self.getToken(BKITParser.DIV_FLOAT, 0)

        def DIV_INT(self):
            return self.getToken(BKITParser.DIV_INT, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 413
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 398
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 399
                        self.match(BKITParser.MUL_FLOAT)
                        self.state = 400
                        self.exp4()
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 401
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 402
                        self.match(BKITParser.MUL_INT)
                        self.state = 403
                        self.exp4()
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 404
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 405
                        self.match(BKITParser.DIV_FLOAT)
                        self.state = 406
                        self.exp4()
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 407
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 408
                        self.match(BKITParser.DIV_INT)
                        self.state = 409
                        self.exp4()
                        pass

                    elif la_ == 5:
                        localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(BKITParser.MOD)
                        self.state = 412
                        self.exp4()
                        pass

             
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp4)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(BKITParser.NOT)
                self.state = 419
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.LP, BKITParser.LB, BKITParser.SUB_INT, BKITParser.SUB_FLOAT, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.STRING_LIT, BKITParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_FLOAT(self):
            return self.getToken(BKITParser.SUB_FLOAT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB_INT(self):
            return self.getToken(BKITParser.SUB_INT, 0)

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp5)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB_FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.match(BKITParser.SUB_FLOAT)
                self.state = 424
                self.exp5()
                pass
            elif token in [BKITParser.SUB_INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.match(BKITParser.SUB_INT)
                self.state = 426
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.LP, BKITParser.LB, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.STRING_LIT, BKITParser.BOOL_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def element_expression(self):
            return self.getTypedRuleContext(BKITParser.Element_expressionContext,0)


        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operand)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.match(BKITParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 432
                self.match(BKITParser.FLOAT_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 433
                self.function_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 434
                self.element_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 435
                self.match(BKITParser.BOOL_LIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 436
                self.match(BKITParser.STRING_LIT)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 437
                self.array_lit()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 438
                self.match(BKITParser.LP)
                self.state = 439
                self.exp()
                self.state = 440
                self.match(BKITParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[25] = self.exp1_sempred
        self._predicates[26] = self.exp2_sempred
        self._predicates[27] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         




