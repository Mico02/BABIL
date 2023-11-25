import argostranslate.package

def installPkg(from_lang, to_lang):
    print(f"Installing {from_lang}->{to_lang} translation package...")
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
    filter(
        lambda x: x.from_code == from_lang and x.to_code == to_lang, available_packages
    )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    print(f"Installed {from_lang}->{to_lang} translation package.")

#English <-> French
installPkg("en","fr")
installPkg("fr","en")

#English <-> Spanish
installPkg("en","es")
installPkg("es","en")

#English <-> Arabic
installPkg("en","ar")
installPkg("ar","en")

#English <-> Hindi
installPkg("en","hi")
installPkg("hi","en")

#English <-> Chinese
installPkg("en","zh")
installPkg("zh","en")

#English <-> Farsi
installPkg("en","fa")
installPkg("fa","en")