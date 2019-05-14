#ifndef __XREFLECTION_PLATFORM_H__
#define __XREFLECTION_PLATFORM_H__

#ifndef BEGIN_NAMESPACE
#define BEGIN_NAMESPACE(name) namespace name {
#define END_NAMESPACE(name) }
#endif

#undef REFL_32
#undef REFL_64
#undef REFL_WIN
#undef REFL_LINUX
#undef REFL_SOARIS

#ifdef _WIN32
	#define REFL_WIN
	#ifdef _WIN64
		#define REFL_64
	#else
		#define REFL_32
	#endif
#elif defined _SUSE_LINUX || defined __linux__
	#define REFL_LINUX
	# if __WORDSIZE == 64
		#define REFL_64
	#else
		#define REFL_32
	#endif
#else
	#define REFL_SOARIS
	#ifdef _LP64
	#define REFL_64
	#else
	#define REFL_32
	#endif
#endif

#ifdef REFL_WIN
	#define REFL_EXPORT __declspec(dllexport)
#elif defined(REFL_LINUX)
	#define REFL_EXPORT __attribute__ ((visibility("default")))
#elif defined(REFL_SOARIS)
	#define REFL_EXPORT __symbolic
#else
	#define REFL_EXPORT
#endif

#ifdef REFL_WIN
	#define REFL_IMPORT __declspec(dllimport)
#elif defined(REFL_LINUX)
	#define REFL_IMPORT __attribute__ ((visibility("default")))
#elif defined(REFL_SOARIS)
	#define REFL_IMPORT __global
#else
	#define REFL_IMPORT
#endif

#endif //__XREFLECTION_PLATFORM_H__
