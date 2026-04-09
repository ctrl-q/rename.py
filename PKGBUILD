pkgname=rename.py
pkgver=0.0.1
pkgrel=1
arch=('any')
depends=('python')
source=('main.py')
sha512sums=('SKIP')

package(){
	install -d "${pkgdir}/usr/local/bin"
	ln -s "$(dirname ${srcdir})/main.py" "${pkgdir}/usr/local/bin/${pkgname}"
}

