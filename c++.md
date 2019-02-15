c++
=
[Standard C++ Library reference](http://www.cplusplus.com/reference/)

## c++ 中使用模板支持 lambda 函数
```c++
template<class _fn1>
std::string regex_search_and_replace(const std::string &str, const char *re,  _fn1 _func)
{
	if (str.empty() || NULL == re || strlen(re) == 0)
	{
		return "";
	}

	const std::regex::flag_type ignorecase = std::regex::icase | std::regex::ECMAScript;

	std::ostringstream outstr;
	std::string::const_iterator it = str.cbegin(), end = str.cend();

	std::smatch match;
	for (; std::regex_search(it, end, match, std::regex(re, ignorecase)); it = match[0].second)
	{
		outstr << match.prefix();
		outstr << _func(match.str().data());
	}

	if (!match.empty())
	{
		outstr << match.suffix();
	}
	else
	{
		outstr << str;
	}

	return outstr.str();
}
```

使用
```c++
sql = regex_search_and_replace(sqlInfo.sql, "\\b(0x[0-9a-fA-F]+)\\b", [](const char *value){
	return hex_to_decimal(value);
});
```

## std::vector 去重
```c++
void UdaoWorkerRepos::GetAllProjects(std::vector< std::string > &projects)
{
    std::for_each(g_workerInfos.begin(), g_workerInfos.end(), [&](const WorkerInfo& o) {
        projects.push_back(o.dllName);
    });

    std::sort(projects.begin(), projects.end());
    std::vector<std::string>::iterator pos = std::unique(projects.begin(), projects.end());
    if (pos != projects.end())
    {
        projects.erase(pos, projects.end());
    }
}
```

## string类成员函数 find 和 find_first_of 的区别
```c++
string s = "abc";
cout << s.find("ad") << endl; 			// 将打印 string::npos 也就是找不到
cout << s.find_first_of("ad") << endl;  //将打印0，也就是找到了，在第0个位置
```

## std::list<std::string> 用逗号join操作，去掉最后一个逗号
```c++
void CInputParamSerialization::Serial(std::map<std::string, std::list<std::string>> &useCases)
{
	std::ostringstream out;
	out << "{" << std::endl;
	std::map<std::string, std::list<std::string>>::iterator itr = useCases.begin();
	for (; itr != m_useCases.end(); itr++)
	{
		out << "\t\"" << itr->first << "\": [" << std::endl;
		
		std::list<std::string>::iterator itrCase = itr->second.begin();
		for (; itrCase != std::prev(itr->second.end()); itrCase ++)
		{
			out << "\t\t" << itrCase->c_str() << "," << std::endl;
		}

		out << "\t\t" << itrCase->c_str() << std::endl;
		out << "\t]" << std::endl;
	}
	out << "}" << std::endl;

	std::cout << out.str();
}
```

## std::string 的 back 与 pop_back 操作
```c++
std::string temp = "xxxxxxxx,"
if (temp.back() == ",")
{
	temp.pop_back();
}
```
