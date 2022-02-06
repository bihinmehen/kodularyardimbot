def blokGetir(isim):
    isim = str(isim).lower()
    match isim:
        case "if":
            return "https://docs.kodular.io/assets/images/blocks/control/if.png"
        case "if else":
            return "https://docs.kodular.io/assets/images/blocks/control/ifelse.png"
        case "if else if":
            return "https://docs.kodular.io/assets/images/blocks/control/if.gif"
        case "for each from to":
            return "https://docs.kodular.io/assets/images/blocks/control/forrange.png"
        case "for each in list":
            return "https://docs.kodular.io/assets/images/blocks/control/foreach.png"
        case "for each key with value in dictionary":
            return "https://docs.kodular.io/assets/images/blocks/control/controls_for_each_dict.png"
        case "while":
            return "https://docs.kodular.io/assets/images/blocks/control/while.png"
        case "if then else":
            return "https://docs.kodular.io/assets/images/blocks/control/choose.png"
        case "do":
            return "https://docs.kodular.io/assets/images/blocks/control/doreturn.png"
        case "evaluate but ignore result":
            return "https://docs.kodular.io/assets/images/blocks/control/evaluate.png"
        case "open another screen":
            return "https://docs.kodular.io/assets/images/blocks/control/openscreen.png"
        case "open another screen with start value":
            return "https://docs.kodular.io/assets/images/blocks/control/openscreenwithvalue.png"
        case "get start value":
            return "https://docs.kodular.io/assets/images/blocks/control/getstartvalue.png"
        case "close screen":
            return "https://docs.kodular.io/assets/images/blocks/control/closescreen.png"
        case "close screen with value":
            return "https://docs.kodular.io/assets/images/blocks/control/closescreenwithvalue.png"
        case "close application" | "close app":
            return "https://docs.kodular.io/assets/images/blocks/control/closeapp.png"
        case "get plain start text":
            return "https://docs.kodular.io/assets/images/blocks/control/getplainstarttext.png"
        case "close screen with plain text":
            return "https://docs.kodular.io/assets/images/blocks/control/closescreenwithplaintext.png"
        case "break":
            return "https://docs.kodular.io/assets/images/blocks/control/break.png"
        case "true":
            return "https://docs.kodular.io/assets/images/blocks/logic/true.png"
        case "false":
            return "https://docs.kodular.io/assets/images/blocks/logic/false.png"
        case "not":
            return "https://docs.kodular.io/assets/images/blocks/logic/not.png"
        case "==" | "=":
            return "https://docs.kodular.io/assets/images/blocks/logic/equals.png"
        case "!==" | "!=":
            return "https://docs.kodular.io/assets/images/blocks/logic/notequals.png"
        case "and":
            return "https://docs.kodular.io/assets/images/blocks/logic/and.png"
        case "or":
            return "https://docs.kodular.io/assets/images/blocks/logic/or.png"
        case "math":
            return "https://docs.kodular.io/assets/images/blocks/math/equals.gif"
        case "min" | "max" | "min max":
            return "https://docs.kodular.io/assets/images/blocks/math/minmax.gif"
        case "square root" | "absolute" | "neg" | "log" | "e^" | "round" | "ceiling" | "floor":
            return "https://docs.kodular.io/assets/images/blocks/math/sqrt.gif"
        case "modulo of" | "remainder of" | "quotient of":
            return "https://docs.kodular.io/assets/images/blocks/math/modulo.gif"
        case "sin" | "cos" | "tan" | "asin" | "acos" | "atan":
            return "https://docs.kodular.io/assets/images/blocks/math/sin.gif"
        case "convert radians to degrees" | "convert degrees to radians":
            return "https://docs.kodular.io/assets/images/blocks/math/convert.gif"
        case "number":
            return "https://docs.kodular.io/assets/images/blocks/math/number.png"
        case "== m" | "= m":
            return "https://docs.kodular.io/assets/images/blocks/math/equal.png"
        case "!== m" | "!= m":
            return "https://docs.kodular.io/assets/images/blocks/math/notequal.png"
        case ">" | "> m":
            return "https://docs.kodular.io/assets/images/blocks/math/greater.png"
        case ">= m" | ">== m" | ">=" | ">==":
            return "https://docs.kodular.io/assets/images/blocks/math/greaterequal.png"
        case ">" | "> m":
            return "https://docs.kodular.io/assets/images/blocks/math/less.png"
        case "<= m" | "<== m" | "<=" | "<==":
            return "https://docs.kodular.io/assets/images/blocks/math/lessequal.png"
        case "+" | "+ m":
            return "https://docs.kodular.io/assets/images/blocks/math/plus.gif"
        case "-" | "- m":
            return "https://docs.kodular.io/assets/images/blocks/math/minus.png"
        case "x" | "x m":
            return "https://docs.kodular.io/assets/images/blocks/math/multiply.gif"
        case "/" | "/ m":
            return "https://docs.kodular.io/assets/images/blocks/math/divide.png"
        case "^" | "^ m":
            return "https://docs.kodular.io/assets/images/blocks/math/exponent.png"
        case "bitwise and":
            return "https://docs.kodular.io/assets/images/blocks/math/bitwise_and.png"
        case "bitwise or":
            return "https://docs.kodular.io/assets/images/blocks/math/bitwise_ior.png"
        case "bitwise xor":
            return "https://docs.kodular.io/assets/images/blocks/math/bitwise_xor.png"
        case "random integer":
            return "https://docs.kodular.io/assets/images/blocks/math/randomint.png"
        case "random fraction":
            return "https://docs.kodular.io/assets/images/blocks/math/randomfrac.png"
        case "random set seed to":
            return "https://docs.kodular.io/assets/images/blocks/math/randomseed.png"
        case "atan2" | "atan2 m":
            return "https://docs.kodular.io/assets/images/blocks/math/atan2.png"
        case "format as decimal":
            return "https://docs.kodular.io/assets/images/blocks/math/format.png"
        case "is a number" | "number?" | "base10?" | "hexadecimal?" | "binary?" | "number" | "base10" | "hexadecimal" | "binary":
            return "https://docs.kodular.io/assets/images/blocks/math/isnumber.png"
        case "convert number" | "base 10 to hex" | "hex to base 10" | "base 10 to binary" | "binary to base 10":
            return "https://docs.kodular.io/assets/images/blocks/math/convertnumber.png"
        case "text" | '""':
            return "https://docs.kodular.io/assets/images/blocks/text/string.png"
        case "join":
            return "https://docs.kodular.io/assets/images/blocks/text/join.png"
        case "lenght" | "len":
            return "https://docs.kodular.io/assets/images/blocks/text/length.png"
        case "is empty" | "empty?" | "is empty?":
            return "https://docs.kodular.io/assets/images/blocks/text/isempty.png"
        case "is string" | "is string?" | "string?":
            return "https://docs.kodular.io/assets/images/blocks/text/isstring.png"
        case "compare texts" | "compare":
            return "https://docs.kodular.io/assets/images/blocks/text/compare.gif"
        case "trim":
            return "https://docs.kodular.io/assets/images/blocks/text/trim.png"
        case "upcase":
            return "https://docs.kodular.io/assets/images/blocks/text/upcase.png"
        case "downcase":
            return "https://docs.kodular.io/assets/images/blocks/text/downcase.png"
        case "starts at" | "starts at text":
            return "https://docs.kodular.io/assets/images/blocks/text/startsat.png"
        case "contains" | "contain" | "contains text" | "contain text":
            return "https://docs.kodular.io/assets/images/blocks/text/contains.png"
        case "split at first" | "split at first text":
            return "https://docs.kodular.io/assets/images/blocks/text/splitatfirst.png"
        case "split at first any" | "split at first any text":
            return "https://docs.kodular.io/assets/images/blocks/text/splitAtFirstOfAny.png"
        case "split" | "split text":
            return "https://docs.kodular.io/assets/images/blocks/text/split.png"
        case "split at any" | "split at any text":
            return "https://docs.kodular.io/assets/images/blocks/text/splitAtAny.png"
        case "split at spaces":
            return "https://docs.kodular.io/assets/images/blocks/text/splitatspaces.png"
        case "segment" | "segment text":
            return "https://docs.kodular.io/assets/images/blocks/text/segment.png"
        case "replace all" | "replace all text" | "replace text" | "replace":
            return "https://docs.kodular.io/assets/images/blocks/text/replaceall.png"
        case "obfuscated" | "obfuscated text":
            return "https://docs.kodular.io/assets/images/blocks/text/obfuscated.png"
        case "create empty list" | "empty list":
            return "https://docs.kodular.io/assets/images/blocks/lists/emptylist.png"
        case "make a list" | "make list":
            return "https://docs.kodular.io/assets/images/blocks/lists/makealist.png"
        case "add item to list":
            return "https://docs.kodular.io/assets/images/blocks/lists/additems.png"
        case "is in list?" | "is in list" | "is in list thing":
            return "https://docs.kodular.io/assets/images/blocks/lists/inlist.png"
        case "length of list":
            return "https://docs.kodular.io/assets/images/blocks/lists/lengthoflist.png"
        case "is list empty" | "is list empty?":
            return "https://docs.kodular.io/assets/images/blocks/lists/islistempty.png"
        case "pick a random item" | "pick a random item list":
            return "https://docs.kodular.io/assets/images/blocks/lists/pickrandomitem.png"
        case "index in list" | "index in list thing":
            return "https://docs.kodular.io/assets/images/blocks/lists/indexinlist.png"
        case "select list item":
            return "https://docs.kodular.io/assets/images/blocks/lists/selectlistitem.png"
        case "insert list item":
            return "https://docs.kodular.io/assets/images/blocks/lists/insert.png"
        case "replace list item":
            return "https://docs.kodular.io/assets/images/blocks/lists/replace.png"
        case "remove list item":
            return "https://docs.kodular.io/assets/images/blocks/lists/removeitem.png"
        case "append to list" | "append list":
            return "https://docs.kodular.io/assets/images/blocks/lists/append.png"
        case "copy list":
            return "https://docs.kodular.io/assets/images/blocks/lists/copy.png"
        case "is a list" | "is a list?" | "is a list thing":
            return "https://docs.kodular.io/assets/images/blocks/lists/isalist.png"
        case "reverse list":
            return "https://docs.kodular.io/assets/images/blocks/lists/reverse.png"
        case "list to csv row":
            return "https://docs.kodular.io/assets/images/blocks/lists/listtocsvrow.png"
        case "list to csv table":
            return "https://docs.kodular.io/assets/images/blocks/lists/listtocsvtable.png"
        case "look up in pairs" | "look up in pairs key":
            return "https://docs.kodular.io/assets/images/blocks/lists/lookupinpairs.png"
        case "join items using separator":
            return "https://docs.kodular.io/assets/images/blocks/lists/joinwithseparator.png"
        case "create empty dictionary" | "empty dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/create-with.png"
        case "make a dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/make-a-dictionary.png"
        case "pair":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/pair.png"
        case "get value for key":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/get-value-for-key.png"
        case "set value for key":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/set-value-for-key.png"
        case "delete entry for key":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/delete-value-for-key.png"
        case "get value at key path":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/get-value-at-key-path.png"
        case "set value for key path":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/set-value-for-key-path.png"
        case "get keys":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/get-keys.png"
        case "get values":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/get-values.png"
        case "is key in dictionary" | "is key in dictionary?":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/is-key-in.png"
        case "size of dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/size.png"
        case "list of pairs to dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/alist-to-dict.png"
        case "dictionary to list of pairs":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/dict-to-alist.png"
        case "copy dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/copy-dict.png"
        case "merge into dictionary":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/combine-dicts.png"
        case "list by walking key path":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/walk-tree.png"
        case "walk all at level":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/walk-all.png"
        case "is a dictionary" | "is a dictionary?":
            return "https://docs.kodular.io/assets/images/blocks/dictionaries/is-dict.png"
        case "color" | "basic color blocks":
            return "https://docs.kodular.io/assets/images/blocks/colors/colorblock.gif"
        case "make color":
            return "https://docs.kodular.io/assets/images/blocks/colors/makecolor.png"
        case "split color":
            return "https://docs.kodular.io/assets/images/blocks/colors/splitcolor.png"
        case "variable" | "initialize global name to":
            return "https://docs.kodular.io/assets/images/blocks/variables/initializeglobal.png"
        case "get":
            return "https://docs.kodular.io/assets/images/blocks/variables/get.png"
        case "set" | "set to":
            return "https://docs.kodular.io/assets/images/blocks/variables/set.png"
        case "initialize local name to do" | "do variable":
            return "https://docs.kodular.io/assets/images/blocks/variables/initializelocaldo.png"
        case "initialize local name to return" | "return variable":
            return "https://docs.kodular.io/assets/images/blocks/variables/initializelocalreturn.png"
        case "procedure do":
            return "https://docs.kodular.io/assets/images/blocks/procedure/do.png"
        case "procedure":
            return "https://docs.kodular.io/assets/images/blocks/procedure/calldo.png"
        case "procedure return":
            return "https://docs.kodular.io/assets/images/blocks/procedure/return.png"
        case "procedure result":
            return "https://docs.kodular.io/assets/images/blocks/procedure/callreturn.png"

    return f"{isim} bulunamadı"
