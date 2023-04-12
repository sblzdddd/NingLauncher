# Retard Donovan's Launcher Core Library
import os
import json


class NLCore:

    def __init__(self, version='1.19.3', minecraft_dir='./.minecraft', minMem='256m', maxMem='8192m',
                 width="854", height="480", os_name="windows", os_version="10", os_arch="x64", username='sblzdddd',
                 uuid="0", accessToken="0", xuid="0", clientID="0", userType="Legacy", launcher_name="NingLauncher",
                 launcher_version="100", wrapper_dir="./wrapper/JavaWrapper.jar"):
        # game version
        self.version = version

        # dirs
        self.minecraft_dir = os.path.abspath(minecraft_dir).replace('\\', "/")
        self.wrapper_dir = os.path.abspath(wrapper_dir).replace('\\', "/")

        self.version_dir = os.path.join(self.minecraft_dir, f"versions\\{self.version}").replace('\\', "/")
        self.native_dir = os.path.join(self.version_dir, f"{self.version}-natives").replace('\\', "/")
        self.libraries_dir = os.path.join(self.minecraft_dir, "libraries").replace('\\', "/")
        self.assets_dir = os.path.join(self.minecraft_dir, "assets").replace('\\', "/")

        # settings
        self.minMem = minMem
        self.maxMem = maxMem
        self.width = width
        self.height = height
        self.features = ["has_custom_resolution"]

        # auth
        self.username = username
        self.uuid = uuid
        self.accessToken = accessToken
        self.clientID = clientID
        self.xuid = xuid
        self.userType = userType

        # system
        self.os_name = os_name
        self.os_version = os_version
        self.os_arch = os_arch

        self.launcher_name = launcher_name
        self.launcher_version = launcher_version

        self.pre_params = ' -XX:+UseG1GC -XX:-UseAdaptiveSizePolicy -XX:-OmitStackTraceInFastThrow' \
                          ' -Dfml.ignoreInvalidMinecraftCertificates=True -Dfml.ignorePatchDiscrepancies=True' \
                          ' -Dlog4j2.formatMsgNoLookups=true'

        with open(f"{minecraft_dir}/versions/{version}/{version}.json", "r") as f:
            self.metadata = json.load(f)

        self.assets_index = self.metadata["assets"]

        self.replaces = {"${natives_directory}": f'"{self.native_dir}"', "${launcher_name}": self.launcher_name,
                         "${launcher_version}": self.launcher_version, "${auth_player_name}": self.username,
                         "${version_name}": self.version, "${game_directory}": f'"{self.minecraft_dir}"',
                         "${assets_root}": f'"{self.assets_dir}"', "${assets_index_name}": self.assets_index,
                         "${auth_uuid}": self.uuid, "${auth_access_token}": self.accessToken,
                         "${clientid}": self.clientID, "${auth_xuid}": self.xuid,
                         "${user_type}": self.userType, "${version_type}": self.launcher_name,
                         "${resolution_width}": self.width, "${resolution_height}": self.height}


    def rules_detect(self, rules):
        for rule in rules:
            if rule["action"] == 'allow':
                if "os" in rule:
                    os_rule = rule["os"]
                    if "name" in os_rule and os_rule["name"] == self.os_name:
                        return True
                    if "arch" in os_rule and os_rule["arch"] == self.os_arch:
                        return True
                elif "features" in rule:
                    for feature in rule["features"].keys():
                        if feature in self.features and rule["features"][feature]:
                            return True
        return False

    def generate_args(self, argType):
        params = []
        args = self.metadata["arguments"][argType]
        for arg in args:
            # if only string, just append it
            if isinstance(arg, str):
                params.append(arg)
            # if it's dict, there are rules
            elif isinstance(arg, dict) and "rules" in arg and self.rules_detect(arg["rules"]):
                val = arg["value"]
                if isinstance(val, str):
                    params.append(val)
                elif isinstance(val, list):
                    for i in val:
                        params.append(i)

        for index, param in enumerate(params):
            for i in self.replaces.keys():
                param = param.replace(i, self.replaces[i])
            params[index] = param
        return params

    # resolve libraries needed for the game and add into params
    def parse_libs(self):
        lib_params = []
        libs = self.metadata["libraries"]
        for lib in libs:
            if "downloads" in lib:
                if "rules" in lib:
                    if self.rules_detect(lib["rules"]):
                        lib_params.append(lib['downloads']['artifact']['path'])
                else:
                    lib_params.append(lib['downloads']['artifact']['path'])

        # convert to absolute path
        for index, param in enumerate(lib_params):
            lib_params[index] = os.path.join(self.libraries_dir, param).replace('\\', "/")

        # also add the version/version.jar
        lib_params.append(os.path.join(self.version_dir, f"{self.version}.jar").replace('\\', "/"))
        libStr = ";".join(lib_params)
        return libStr

    def generate_params(self):
        libParams = self.parse_libs()
        jvmParams = self.generate_args("jvm")
        for index, param in enumerate(jvmParams):
            param = param.replace("${classpath}", f'"{libParams}"')
            jvmParams[index] = param

        # fuck you Mojang!!!
        jvmParams[1] = jvmParams[1].replace("Windows 10", '"Windows 10"')
        jvmParams.append(f'-Xmn{self.minMem}')
        jvmParams.append(f'-Xmx{self.maxMem}')
        jvmParams.append(f'-jar "{self.wrapper_dir}"')
        jvmParams = " ".join(jvmParams)

        # parse game params
        gameParams = self.generate_args("game")
        gameParams = " ".join(gameParams)

        mainClass = self.metadata['mainClass']

        AllArguments = f"{jvmParams} {mainClass} {gameParams}"

        return AllArguments


if __name__ == "__main__":
    nlc = NLCore()
    print(nlc.generate_params())
