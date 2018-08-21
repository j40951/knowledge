import os
import sys
import json
import re
import platform
import time
import getopt
import zipfile

from distutils.core import setup

USAGE = """\
usage: %(script)s install
   or: %(script)s dist
"""

err_list = []

def check_info(_dist_info):
    if _dist_info is None:
        _err = 'parameter is None'
        return _err
    if 'name' not in _dist_info:
        _err = "'name' not in setup file"
        return _err
    if 'version' not in _dist_info:
        _err = "'version' not in setup file"
        return _err
    if 'os' not in _dist_info:
        _err = "'os' not in setup file"
        return _err
    if 'dist' not in _dist_info:
        _err = "'dist' not in setup file"
        return _err
    return None


def get_usage(script_name):
    script = os.path.basename(script_name)
    return USAGE % {'script': script}


def parse_rule(_rule):
    if _rule is None:
        _err = 'parameter is invalid'
        return None, _err
    _result = dict()
    _pattern = re.compile(r'^([a-zA-Z0-9-_/.]+)/([*]{1,2})([a-zA-Z0-9-_.,]*)$')
    _match = _pattern.match(_rule)
    if _match:
        _group = _match.groups()
        _result['dir'] = _group[0]
        if _group[1].count('*') == 2:
            _result['recursive'] = True
        else:
            _result['recursive'] = False
        if len(_group) == 3:
            _result['suffix'] = _group[2].split(',')

    else:
        _err = 'match fail, rule = %s' % _rule
        return None, _err
    return _result, None


def zip_dist(_dist_info):
    if _dist_info is None or 'dist' not in _dist_info:
        _err = 'parameter is invalid'
        return None, _err
    _zip_target = list()
    for _dist_type in _dist_info['dist']:
        if 'arc' in _dist_info['dist'][_dist_type]:
            _arc = _dist_info['dist'][_dist_type]['arc']
        else:
            _arc = ''

        if 'pattern' in _dist_info['dist'][_dist_type]:
            _patterns = _dist_info['dist'][_dist_type]['pattern']
            for _item in _patterns:
                # print _item
                _rule, _err = parse_rule(_item)
                if _err is None:
                    if _arc is not None:
                        _rule['arc'] = _arc
                    # print 'success->', _rule
                    _zip_target.append(_rule)
                else:
                    # print _err
                    err_list.append('Parse rule fail, item=%s, err=%s' % (_item, _err))
    return _zip_target, None


def walk_dir_and_zip(_zip_filename, _zip_target):
    _zip_file = 'dist/%s.zip' % _zip_filename
    zip_file = zipfile.ZipFile(_zip_file, mode='w', compression=zipfile.ZIP_DEFLATED)
    try:
        for _target in _zip_target:
            _dir, _file_list, _arc, _err = walk_dir(_target)
            if _err is not None:
                # print 'Error->', _err
                err_list.append('%s walk fail, err=%s' % (_target, _err))
                continue

            for _file in _file_list:
                _arc_name = _zip_filename + os.sep + _arc + _file.replace(_dir, '', 1)
                # print _dir
                print _file
                print 'ar->', _arc_name
                zip_file.write(_file, arcname=_arc_name)
    finally:
        zip_file.close()


def walk_dir(_target):
    if 'dir' not in _target or 'recursive' not in _target:
        _err = "'dir' or 'recursive' not in target"
        return None, None, None, _err

    _dir = _target['dir']
    _recursive = _target['recursive']

    if 'arc' in _target:
        _arc = _target['arc']
    else:
        _arc = None

    if 'suffix' in _target:
        _suffix = _target['suffix']
    else:
        _suffix = None

    _file_list = list()
    for _root, _dirs, _files in os.walk(_dir):
        for _name in _files:
            if _suffix is None:
                _file_list.append(os.path.join(_root, _name))
                continue
            for _item in _suffix:
                if _name == _item or (_item.startswith('.') and _name.endswith(_item)):
                    _file_list.append(os.path.join(_root, _name))
                    break
        for _name in _dirs:
            _file_list.append(os.path.join(_root, _name))

        if not _recursive:
            break

    return _dir, _file_list, _arc, None


def setup(_setup_file):

    if not os.path.exists('dist'):
        os.mkdir('dist')
        
    with open(_setup_file) as f:
        _dist_info = json.load(f)

    _err = check_info(_dist_info)
    if _err is not None:
        # print 'Error: $s, file=%s' % (_err, _setup_file)
        return None, 'Error: $s, file=%s' % (_err, _setup_file)
        # exit()
    _dist_info['build'] = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # print _dist_info
    _zip_filename = '%(name)s-%(os)s-%(version)s.%(build)s' % _dist_info
    _version = '%(version)s.%(build)s' % _dist_info
    # print zip_filename, version
    _zip_target, _err = zip_dist(_dist_info)
    if _err is None:
        # print zip_target
        walk_dir_and_zip(_zip_filename, _zip_target)
        return _zip_filename, None
    return None, _err
    
    
def main():
    _setup_file = 'setup/setup.json'
    if platform.system() == 'Linux':
        _setup_file = 'setup/setup-linux.json'
        
    opts, args = getopt.getopt(sys.argv[1:], "f:", ['file='])
    for op, value in opts:
        if op in ('-f', '--file'):
            _setup_file = value
            
    _target_file, _err = setup(_setup_file)
    if _err is not None:
        print _err
        return
    
    if len(err_list) > 0:
        print '\nError:'
        for _err in err_list:
            print '  ', _err
    else:
        print "\nTarget -> %s" % _target_file
        print '\nSuccess.'

if __name__ == '__main__':
    main()
