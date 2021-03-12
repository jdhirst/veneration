import builtins
builtins.MILLISECOND = 10000
builtins.SECOND = 10000000
builtins.MINUTE = 60*SECOND
builtins.HOUR   = 60*MINUTE
builtins.DAY    = 24*HOUR

__all__ = [
	"blue", "util", "config", "cache", "embedfs",
	"dbutil", "const", "objectCaching", "exceptions", "strings",
	"carbon", "eve",
]
