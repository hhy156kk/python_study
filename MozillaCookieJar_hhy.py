#仿写MozillaCookieJar


from cookielib import FileCookieJar
from cookielib import Cookie
import time


class MozillaCookieJar(FileCookieJar):

    #没有__init__(),默认调用父类__init__()


    header = ""

    def _really_load(self, f, filename, ignore_discard, ignore_expires):
        now = time.time()

        magic = f.readline()
        if not re.search(self.magic_re, magic):
            f.close()
            raise LoadError(
                "%r does not look like a Netscape format cookies file" %
                filename)

        try:
            while 1:
                line = f.readline()
                if line == "": break

                # last field may be absent, so keep any trailing tab
                if line.endswith("\n"): line = line[:-1]

                # skip comments and blank lines XXX what is $ for?
                if (line.strip().startswith(("#", "$")) or
                            line.strip() == ""):
                    continue

                domain, domain_specified, path, secure, expires, name, value = \
                    line.split("\t")
                secure = (secure == "TRUE")
                domain_specified = (domain_specified == "TRUE")
                if name == "":
                    # cookies.txt regards 'Set-Cookie: foo' as a cookie
                    # with no name, whereas cookielib regards it as a
                    # cookie with no value.
                    name = value
                    value = None

                initial_dot = domain.startswith(".")
                assert domain_specified == initial_dot

                discard = False
                if expires == "":
                    expires = None
                    discard = True

                # assume path_specified is false
                c = Cookie(0, name, value,
                           None, False,
                           domain, domain_specified, initial_dot,
                           path, False,
                           secure,
                           expires,
                           discard,
                           None,
                           None,
                           {})
                if not ignore_discard and c.discard:
                    continue
                if not ignore_expires and c.is_expired(now):
                    continue
                self.set_cookie(c)

        except IOError:
            raise
        except Exception:
            _warn_unhandled_exception()
            raise LoadError("invalid Netscape format cookies file %r: %r" %
                            (filename, line))

    def save(self, filename=None, ignore_discard=False, ignore_expires=False):

        if filename is not None:
            if self.filename is not None:
                self.filename = filename
            else:
                raise ValueError("error")

        f = open(filename,"w")
        try:
            f.write(self.header)

            #返回自1970年来的秒数
            now = time.time()

            #使用迭代器范问实例中存储的cookie
            #ignore_discard的意思是即使cookies将被丢弃也将它保存下来
            #ignore_expires的意思是如果在该文件中 cookies已经存在，则覆盖原文件写入

            for cookie in self:
                if not ignore_discard and cookie.discard :
                    continue
                #判断是否过期
                if not ignore_expires and cookie.is_expired(now):
                    continue
                if cookie.secure:
                    secure = True
                if cookie.domain.startswith("."):
                    initial_dot = True
                else:
                    initial_dot = False
                if cookie.expired is not None:
                    expired = str(cookie.expired)
                else:
                    expired = ""
                if cookie.value is None:
                    name = ""
                    value = name
                else
                    name = cookie.name
                    value = cookie.value
                f.write(
                    "\t".join([cookie.domain, initial_dot, cookie.path,
                               secure, expires, name, value]) +
                    "\n")
            finally:
            f.close()






        finally:




