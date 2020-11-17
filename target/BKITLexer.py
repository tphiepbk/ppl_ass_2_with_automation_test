# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0242\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6\u00b7")
        buf.write("\n\6\f\6\16\6\u00ba\13\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\5<\u018b")
        buf.write("\n<\3=\3=\7=\u018f\n=\f=\16=\u0192\13=\3>\3>\3>\3>\5>")
        buf.write("\u0198\n>\3>\3>\7>\u019c\n>\f>\16>\u019f\13>\3?\3?\3@")
        buf.write("\3@\3@\3@\5@\u01a7\n@\3@\3@\7@\u01ab\n@\f@\16@\u01ae\13")
        buf.write("@\3A\3A\3B\3B\3C\3C\5C\u01b6\nC\3C\3C\3C\5C\u01bb\nC\5")
        buf.write("C\u01bd\nC\3D\6D\u01c0\nD\rD\16D\u01c1\3E\3E\7E\u01c6")
        buf.write("\nE\fE\16E\u01c9\13E\3F\3F\5F\u01cd\nF\3F\6F\u01d0\nF")
        buf.write("\rF\16F\u01d1\3G\3G\3G\3G\3G\3G\7G\u01da\nG\fG\16G\u01dd")
        buf.write("\13G\3G\3G\3G\3H\3H\5H\u01e4\nH\3I\3I\3I\3I\3I\3J\3J\3")
        buf.write("J\3J\3J\3J\3K\3K\3K\3K\7K\u01f5\nK\fK\16K\u01f8\13K\3")
        buf.write("K\3K\3K\3K\3K\3L\6L\u0200\nL\rL\16L\u0201\3L\3L\3M\3M")
        buf.write("\3M\3M\3M\3M\7M\u020c\nM\fM\16M\u020f\13M\3M\3M\3M\3M")
        buf.write("\5M\u0215\nM\3M\3M\3M\3N\3N\3N\3N\3N\3N\7N\u0220\nN\f")
        buf.write("N\16N\u0223\13N\3N\3N\3O\3O\3P\3P\3P\3Q\3Q\3Q\3R\3R\3")
        buf.write("R\3R\5R\u0233\nR\3S\3S\3S\3S\7S\u0239\nS\fS\16S\u023c")
        buf.write("\13S\3S\3S\3T\3T\3T\4\u01f6\u023a\2U\3\2\5\2\7\2\t\2\13")
        buf.write("\3\r\4\17\5\21\6\23\7\25\b\27\t\31\n\33\13\35\f\37\r!")
        buf.write("\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67")
        buf.write("\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+")
        buf.write("],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67u8w9y\2{\2}\2")
        buf.write("\177\2\u0081\2\u0083:\u0085;\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("<\u008f=\u0091>\u0093?\u0095@\u0097A\u0099B\u009bC\u009d")
        buf.write("\2\u009f\2\u00a1\2\u00a3\2\u00a5D\u00a7E\3\2\21\3\2c|")
        buf.write("\3\2C\\\3\2\62;\3\2\63;\4\2\63;CH\4\2\62;CH\3\2\639\3")
        buf.write("\2\629\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\6\2\f\f$$))^")
        buf.write("^\5\2\13\f\17\17\"\"\3\2$$\5\2\f\f$$^^\2\u0253\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2")
        buf.write("\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ab\3\2\2\2\7\u00ad")
        buf.write("\3\2\2\2\t\u00af\3\2\2\2\13\u00b1\3\2\2\2\r\u00bb\3\2")
        buf.write("\2\2\17\u00c0\3\2\2\2\21\u00c6\3\2\2\2\23\u00cf\3\2\2")
        buf.write("\2\25\u00d2\3\2\2\2\27\u00d7\3\2\2\2\31\u00de\3\2\2\2")
        buf.write("\33\u00e6\3\2\2\2\35\u00ec\3\2\2\2\37\u00f3\3\2\2\2!\u00fc")
        buf.write("\3\2\2\2#\u0100\3\2\2\2%\u0109\3\2\2\2\'\u010c\3\2\2\2")
        buf.write(")\u0116\3\2\2\2+\u011d\3\2\2\2-\u0122\3\2\2\2/\u0126\3")
        buf.write("\2\2\2\61\u012c\3\2\2\2\63\u0132\3\2\2\2\65\u0134\3\2")
        buf.write("\2\2\67\u0136\3\2\2\29\u0138\3\2\2\2;\u013a\3\2\2\2=\u013c")
        buf.write("\3\2\2\2?\u013e\3\2\2\2A\u0140\3\2\2\2C\u0142\3\2\2\2")
        buf.write("E\u0144\3\2\2\2G\u0146\3\2\2\2I\u0148\3\2\2\2K\u014b\3")
        buf.write("\2\2\2M\u014d\3\2\2\2O\u0150\3\2\2\2Q\u0152\3\2\2\2S\u0155")
        buf.write("\3\2\2\2U\u0157\3\2\2\2W\u015a\3\2\2\2Y\u015c\3\2\2\2")
        buf.write("[\u015e\3\2\2\2]\u0160\3\2\2\2_\u0163\3\2\2\2a\u0166\3")
        buf.write("\2\2\2c\u0169\3\2\2\2e\u016c\3\2\2\2g\u016e\3\2\2\2i\u0170")
        buf.write("\3\2\2\2k\u0173\3\2\2\2m\u0176\3\2\2\2o\u017a\3\2\2\2")
        buf.write("q\u017d\3\2\2\2s\u0180\3\2\2\2u\u0183\3\2\2\2w\u018a\3")
        buf.write("\2\2\2y\u018c\3\2\2\2{\u0197\3\2\2\2}\u01a0\3\2\2\2\177")
        buf.write("\u01a6\3\2\2\2\u0081\u01af\3\2\2\2\u0083\u01b1\3\2\2\2")
        buf.write("\u0085\u01b3\3\2\2\2\u0087\u01bf\3\2\2\2\u0089\u01c3\3")
        buf.write("\2\2\2\u008b\u01ca\3\2\2\2\u008d\u01d3\3\2\2\2\u008f\u01e3")
        buf.write("\3\2\2\2\u0091\u01e5\3\2\2\2\u0093\u01ea\3\2\2\2\u0095")
        buf.write("\u01f0\3\2\2\2\u0097\u01ff\3\2\2\2\u0099\u0205\3\2\2\2")
        buf.write("\u009b\u0219\3\2\2\2\u009d\u0226\3\2\2\2\u009f\u0228\3")
        buf.write("\2\2\2\u00a1\u022b\3\2\2\2\u00a3\u0232\3\2\2\2\u00a5\u0234")
        buf.write("\3\2\2\2\u00a7\u023f\3\2\2\2\u00a9\u00aa\t\2\2\2\u00aa")
        buf.write("\4\3\2\2\2\u00ab\u00ac\t\3\2\2\u00ac\6\3\2\2\2\u00ad\u00ae")
        buf.write("\t\4\2\2\u00ae\b\3\2\2\2\u00af\u00b0\7a\2\2\u00b0\n\3")
        buf.write("\2\2\2\u00b1\u00b8\5\3\2\2\u00b2\u00b7\5\3\2\2\u00b3\u00b7")
        buf.write("\5\5\3\2\u00b4\u00b7\5\7\4\2\u00b5\u00b7\5\t\5\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3")
        buf.write("\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\f\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00bb\u00bc\7D\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7f\2\2\u00be\u00bf\7{\2\2\u00bf\16\3\2\2\2\u00c0\u00c1")
        buf.write("\7D\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7m\2\2\u00c5\20\3\2\2\2\u00c6\u00c7")
        buf.write("\7E\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca")
        buf.write("\7v\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7w\2\2\u00cd\u00ce\7g\2\2\u00ce\22\3\2\2\2\u00cf\u00d0")
        buf.write("\7F\2\2\u00d0\u00d1\7q\2\2\u00d1\24\3\2\2\2\u00d2\u00d3")
        buf.write("\7G\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7u\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\26\3\2\2\2\u00d7\u00d8\7G\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7K\2\2\u00dc\u00dd\7h\2\2\u00dd\30\3\2\2\2\u00de\u00df")
        buf.write("\7G\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1\u00e2")
        buf.write("\7D\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5")
        buf.write("\7{\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7G\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7f\2\2\u00e9\u00ea\7K\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb\34\3\2\2\2\u00ec\u00ed\7G\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0\7H\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7t\2\2\u00f2\36\3\2\2\2\u00f3\u00f4")
        buf.write("\7G\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7f\2\2\u00f6\u00f7")
        buf.write("\7Y\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa")
        buf.write("\7n\2\2\u00fa\u00fb\7g\2\2\u00fb \3\2\2\2\u00fc\u00fd")
        buf.write("\7H\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7t\2\2\u00ff\"")
        buf.write("\3\2\2\2\u0100\u0101\7H\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7p\2\2\u0103\u0104\7e\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7q\2\2\u0107\u0108\7p\2\2\u0108$\3")
        buf.write("\2\2\2\u0109\u010a\7K\2\2\u010a\u010b\7h\2\2\u010b&\3")
        buf.write("\2\2\2\u010c\u010d\7R\2\2\u010d\u010e\7c\2\2\u010e\u010f")
        buf.write("\7t\2\2\u010f\u0110\7c\2\2\u0110\u0111\7o\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7v\2\2\u0113\u0114\7g\2\2\u0114\u0115")
        buf.write("\7t\2\2\u0115(\3\2\2\2\u0116\u0117\7T\2\2\u0117\u0118")
        buf.write("\7g\2\2\u0118\u0119\7v\2\2\u0119\u011a\7w\2\2\u011a\u011b")
        buf.write("\7t\2\2\u011b\u011c\7p\2\2\u011c*\3\2\2\2\u011d\u011e")
        buf.write("\7V\2\2\u011e\u011f\7j\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121,\3\2\2\2\u0122\u0123\7X\2\2\u0123\u0124")
        buf.write("\7c\2\2\u0124\u0125\7t\2\2\u0125.\3\2\2\2\u0126\u0127")
        buf.write("\7Y\2\2\u0127\u0128\7j\2\2\u0128\u0129\7k\2\2\u0129\u012a")
        buf.write("\7n\2\2\u012a\u012b\7g\2\2\u012b\60\3\2\2\2\u012c\u012d")
        buf.write("\7G\2\2\u012d\u012e\7p\2\2\u012e\u012f\7f\2\2\u012f\u0130")
        buf.write("\7F\2\2\u0130\u0131\7q\2\2\u0131\62\3\2\2\2\u0132\u0133")
        buf.write("\7=\2\2\u0133\64\3\2\2\2\u0134\u0135\7<\2\2\u0135\66\3")
        buf.write("\2\2\2\u0136\u0137\7\60\2\2\u01378\3\2\2\2\u0138\u0139")
        buf.write("\7.\2\2\u0139:\3\2\2\2\u013a\u013b\7*\2\2\u013b<\3\2\2")
        buf.write("\2\u013c\u013d\7+\2\2\u013d>\3\2\2\2\u013e\u013f\7]\2")
        buf.write("\2\u013f@\3\2\2\2\u0140\u0141\7_\2\2\u0141B\3\2\2\2\u0142")
        buf.write("\u0143\7}\2\2\u0143D\3\2\2\2\u0144\u0145\7\177\2\2\u0145")
        buf.write("F\3\2\2\2\u0146\u0147\7-\2\2\u0147H\3\2\2\2\u0148\u0149")
        buf.write("\5G$\2\u0149\u014a\5\67\34\2\u014aJ\3\2\2\2\u014b\u014c")
        buf.write("\7/\2\2\u014cL\3\2\2\2\u014d\u014e\5K&\2\u014e\u014f\5")
        buf.write("\67\34\2\u014fN\3\2\2\2\u0150\u0151\7,\2\2\u0151P\3\2")
        buf.write("\2\2\u0152\u0153\5O(\2\u0153\u0154\5\67\34\2\u0154R\3")
        buf.write("\2\2\2\u0155\u0156\7^\2\2\u0156T\3\2\2\2\u0157\u0158\5")
        buf.write("S*\2\u0158\u0159\5\67\34\2\u0159V\3\2\2\2\u015a\u015b")
        buf.write("\7\'\2\2\u015bX\3\2\2\2\u015c\u015d\7?\2\2\u015dZ\3\2")
        buf.write("\2\2\u015e\u015f\7#\2\2\u015f\\\3\2\2\2\u0160\u0161\7")
        buf.write("(\2\2\u0161\u0162\7(\2\2\u0162^\3\2\2\2\u0163\u0164\7")
        buf.write("~\2\2\u0164\u0165\7~\2\2\u0165`\3\2\2\2\u0166\u0167\7")
        buf.write("?\2\2\u0167\u0168\7?\2\2\u0168b\3\2\2\2\u0169\u016a\7")
        buf.write("#\2\2\u016a\u016b\7?\2\2\u016bd\3\2\2\2\u016c\u016d\7")
        buf.write(">\2\2\u016df\3\2\2\2\u016e\u016f\7@\2\2\u016fh\3\2\2\2")
        buf.write("\u0170\u0171\7>\2\2\u0171\u0172\7?\2\2\u0172j\3\2\2\2")
        buf.write("\u0173\u0174\7@\2\2\u0174\u0175\7?\2\2\u0175l\3\2\2\2")
        buf.write("\u0176\u0177\7?\2\2\u0177\u0178\7\61\2\2\u0178\u0179\7")
        buf.write("?\2\2\u0179n\3\2\2\2\u017a\u017b\5e\63\2\u017b\u017c\5")
        buf.write("\67\34\2\u017cp\3\2\2\2\u017d\u017e\5g\64\2\u017e\u017f")
        buf.write("\5\67\34\2\u017fr\3\2\2\2\u0180\u0181\5i\65\2\u0181\u0182")
        buf.write("\5\67\34\2\u0182t\3\2\2\2\u0183\u0184\5k\66\2\u0184\u0185")
        buf.write("\5\67\34\2\u0185v\3\2\2\2\u0186\u018b\5{>\2\u0187\u018b")
        buf.write("\5\177@\2\u0188\u018b\5y=\2\u0189\u018b\5\u0083B\2\u018a")
        buf.write("\u0186\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018a\u0189\3\2\2\2\u018bx\3\2\2\2\u018c\u0190\t\5\2")
        buf.write("\2\u018d\u018f\5\7\4\2\u018e\u018d\3\2\2\2\u018f\u0192")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191")
        buf.write("z\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\7\62\2\2\u0194")
        buf.write("\u0198\7z\2\2\u0195\u0196\7\62\2\2\u0196\u0198\7Z\2\2")
        buf.write("\u0197\u0193\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199\u019d\t\6\2\2\u019a\u019c\5}?\2\u019b\u019a")
        buf.write("\3\2\2\2\u019c\u019f\3\2\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e|\3\2\2\2\u019f\u019d\3\2\2\2\u01a0")
        buf.write("\u01a1\t\7\2\2\u01a1~\3\2\2\2\u01a2\u01a3\7\62\2\2\u01a3")
        buf.write("\u01a7\7q\2\2\u01a4\u01a5\7\62\2\2\u01a5\u01a7\7Q\2\2")
        buf.write("\u01a6\u01a2\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01ac\t\b\2\2\u01a9\u01ab\5\u0081A\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u0080\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01af\u01b0\t\t\2\2\u01b0\u0082\3\2\2\2\u01b1\u01b2")
        buf.write("\7\62\2\2\u01b2\u0084\3\2\2\2\u01b3\u01bc\5\u0087D\2\u01b4")
        buf.write("\u01b6\5\u0089E\2\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2")
        buf.write("\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01bd\5\u008bF\2\u01b8")
        buf.write("\u01ba\5\u0089E\2\u01b9\u01bb\5\u008bF\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01b5")
        buf.write("\3\2\2\2\u01bc\u01b8\3\2\2\2\u01bd\u0086\3\2\2\2\u01be")
        buf.write("\u01c0\t\4\2\2\u01bf\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u0088\3")
        buf.write("\2\2\2\u01c3\u01c7\5\67\34\2\u01c4\u01c6\5\7\4\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u008a\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01ca\u01cc\t\n\2\2\u01cb\u01cd\t\13\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2")
        buf.write("\u01ce\u01d0\5\7\4\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3")
        buf.write("\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u008c")
        buf.write("\3\2\2\2\u01d3\u01db\7$\2\2\u01d4\u01d5\7)\2\2\u01d5\u01da")
        buf.write("\7$\2\2\u01d6\u01d7\7^\2\2\u01d7\u01da\t\f\2\2\u01d8\u01da")
        buf.write("\n\r\2\2\u01d9\u01d4\3\2\2\2\u01d9\u01d6\3\2\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3")
        buf.write("\2\2\2\u01de\u01df\7$\2\2\u01df\u01e0\bG\2\2\u01e0\u008e")
        buf.write("\3\2\2\2\u01e1\u01e4\5\u0091I\2\u01e2\u01e4\5\u0093J\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u0090\3")
        buf.write("\2\2\2\u01e5\u01e6\7V\2\2\u01e6\u01e7\7t\2\2\u01e7\u01e8")
        buf.write("\7w\2\2\u01e8\u01e9\7g\2\2\u01e9\u0092\3\2\2\2\u01ea\u01eb")
        buf.write("\7H\2\2\u01eb\u01ec\7c\2\2\u01ec\u01ed\7n\2\2\u01ed\u01ee")
        buf.write("\7u\2\2\u01ee\u01ef\7g\2\2\u01ef\u0094\3\2\2\2\u01f0\u01f1")
        buf.write("\7,\2\2\u01f1\u01f2\7,\2\2\u01f2\u01f6\3\2\2\2\u01f3\u01f5")
        buf.write("\13\2\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6")
        buf.write("\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f9\3\2\2\2")
        buf.write("\u01f8\u01f6\3\2\2\2\u01f9\u01fa\7,\2\2\u01fa\u01fb\7")
        buf.write(",\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\bK\3\2\u01fd\u0096")
        buf.write("\3\2\2\2\u01fe\u0200\t\16\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2")
        buf.write("\u0202\u0203\3\2\2\2\u0203\u0204\bL\3\2\u0204\u0098\3")
        buf.write("\2\2\2\u0205\u020d\7$\2\2\u0206\u0207\7)\2\2\u0207\u020c")
        buf.write("\7$\2\2\u0208\u0209\7^\2\2\u0209\u020c\t\f\2\2\u020a\u020c")
        buf.write("\n\r\2\2\u020b\u0206\3\2\2\2\u020b\u0208\3\2\2\2\u020b")
        buf.write("\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2")
        buf.write("\u020d\u020e\3\2\2\2\u020e\u0214\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u0210\u0211\7^\2\2\u0211\u0215\n\f\2\2\u0212\u0213")
        buf.write("\7)\2\2\u0213\u0215\n\17\2\2\u0214\u0210\3\2\2\2\u0214")
        buf.write("\u0212\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\7$\2\2")
        buf.write("\u0217\u0218\bM\4\2\u0218\u009a\3\2\2\2\u0219\u0221\7")
        buf.write("$\2\2\u021a\u021b\7)\2\2\u021b\u0220\7$\2\2\u021c\u021d")
        buf.write("\7^\2\2\u021d\u0220\t\f\2\2\u021e\u0220\n\r\2\2\u021f")
        buf.write("\u021a\3\2\2\2\u021f\u021c\3\2\2\2\u021f\u021e\3\2\2\2")
        buf.write("\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3")
        buf.write("\2\2\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225")
        buf.write("\bN\5\2\u0225\u009c\3\2\2\2\u0226\u0227\n\20\2\2\u0227")
        buf.write("\u009e\3\2\2\2\u0228\u0229\7^\2\2\u0229\u022a\t\f\2\2")
        buf.write("\u022a\u00a0\3\2\2\2\u022b\u022c\7)\2\2\u022c\u022d\7")
        buf.write("$\2\2\u022d\u00a2\3\2\2\2\u022e\u022f\7^\2\2\u022f\u0233")
        buf.write("\n\f\2\2\u0230\u0231\7)\2\2\u0231\u0233\n\17\2\2\u0232")
        buf.write("\u022e\3\2\2\2\u0232\u0230\3\2\2\2\u0233\u00a4\3\2\2\2")
        buf.write("\u0234\u0235\7,\2\2\u0235\u0236\7,\2\2\u0236\u023a\3\2")
        buf.write("\2\2\u0237\u0239\13\2\2\2\u0238\u0237\3\2\2\2\u0239\u023c")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b")
        buf.write("\u023d\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u023e\bS\6\2")
        buf.write("\u023e\u00a6\3\2\2\2\u023f\u0240\13\2\2\2\u0240\u0241")
        buf.write("\bT\7\2\u0241\u00a8\3\2\2\2\36\2\u00b6\u00b8\u018a\u0190")
        buf.write("\u0197\u019d\u01a6\u01ac\u01b5\u01ba\u01bc\u01c1\u01c7")
        buf.write("\u01cc\u01d1\u01d9\u01db\u01e3\u01f6\u0201\u020b\u020d")
        buf.write("\u0214\u021f\u0221\u0232\u023a\b\3G\2\b\2\2\3M\3\3N\4")
        buf.write("\3S\5\3T\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BODY = 2
    BREAK = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    ELSEIF = 7
    ENDBODY = 8
    ENDIF = 9
    ENDFOR = 10
    ENDWHILE = 11
    FOR = 12
    FUNCTION = 13
    IF = 14
    PARAMETER = 15
    RETURN = 16
    THEN = 17
    VAR = 18
    WHILE = 19
    ENDDO = 20
    SEMI = 21
    COLON = 22
    DOT = 23
    COMMA = 24
    LP = 25
    RP = 26
    LSB = 27
    RSB = 28
    LB = 29
    RB = 30
    ADD_INT = 31
    ADD_FLOAT = 32
    SUB_INT = 33
    SUB_FLOAT = 34
    MUL_INT = 35
    MUL_FLOAT = 36
    DIV_INT = 37
    DIV_FLOAT = 38
    MOD = 39
    ASSIGN = 40
    NOT = 41
    AND = 42
    OR = 43
    EQUAL = 44
    NOTEQUAL_INT = 45
    LT_INT = 46
    GT_INT = 47
    LTE_INT = 48
    GTE_INT = 49
    NOTEQUAL_FLOAT = 50
    LT_FLOAT = 51
    GT_FLOAT = 52
    LTE_FLOAT = 53
    GTE_FLOAT = 54
    INT_LIT = 55
    ZERO_LIT = 56
    FLOAT_LIT = 57
    STRING_LIT = 58
    BOOL_LIT = 59
    TRUE = 60
    FALSE = 61
    COMMENT = 62
    WS = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    UNTERMINATED_COMMENT = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "';'", "':'", "'.'", "','", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=/='", "'0'", "'True'", "'False'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "SEMI", "COLON", 
            "DOT", "COMMA", "LP", "RP", "LSB", "RSB", "LB", "RB", "ADD_INT", 
            "ADD_FLOAT", "SUB_INT", "SUB_FLOAT", "MUL_INT", "MUL_FLOAT", 
            "DIV_INT", "DIV_FLOAT", "MOD", "ASSIGN", "NOT", "AND", "OR", 
            "EQUAL", "NOTEQUAL_INT", "LT_INT", "GT_INT", "LTE_INT", "GTE_INT", 
            "NOTEQUAL_FLOAT", "LT_FLOAT", "GT_FLOAT", "LTE_FLOAT", "GTE_FLOAT", 
            "INT_LIT", "ZERO_LIT", "FLOAT_LIT", "STRING_LIT", "BOOL_LIT", 
            "TRUE", "FALSE", "COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", "UNDERSCORE", 
                  "ID", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                  "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                  "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
                  "SEMI", "COLON", "DOT", "COMMA", "LP", "RP", "LSB", "RSB", 
                  "LB", "RB", "ADD_INT", "ADD_FLOAT", "SUB_INT", "SUB_FLOAT", 
                  "MUL_INT", "MUL_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", 
                  "ASSIGN", "NOT", "AND", "OR", "EQUAL", "NOTEQUAL_INT", 
                  "LT_INT", "GT_INT", "LTE_INT", "GTE_INT", "NOTEQUAL_FLOAT", 
                  "LT_FLOAT", "GT_FLOAT", "LTE_FLOAT", "GTE_FLOAT", "INT_LIT", 
                  "DECIMAL", "HEX", "HEX_DIGIT", "OCTAL", "OCTAL_DIGIT", 
                  "ZERO_LIT", "FLOAT_LIT", "INT_PART", "DEC_PART", "EXP_PART", 
                  "STRING_LIT", "BOOL_LIT", "TRUE", "FALSE", "COMMENT", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STR_CHAR", 
                  "ESC_SEQ", "DOUBLE_QUOTE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[69] = self.STRING_LIT_action 
            actions[75] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[81] = self.UNTERMINATED_COMMENT_action 
            actions[82] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = self.text[1:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    raise IllegalEscape(self.text[1:])
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    raise UncloseString(self.text[1:])
                
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UnterminatedComment()
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    raise ErrorToken(self.text[0:])
                
     


