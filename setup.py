import setuptools
import cpymake
import cpymake.command.build_ext

setuptools.setup(
    ext_modules = [cpymake.Extension("apep.ml.genetic", "apep_genetic")],
    cmdclass = {"build_ext": cpymake.command.build_ext.build_ext}
    )
