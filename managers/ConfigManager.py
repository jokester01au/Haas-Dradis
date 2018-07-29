from authentication.models import ConfigurationModel


class ConfigManager:

    @staticmethod
    def get_or_create_config():
        try:
            configModel = ConfigurationModel.objects.get()
            return configModel

        except:
            configModel = ConfigurationModel()
            configModel.haasIp = ""
            configModel.haasPort = 8060
            configModel.haasSecret = ""
            configModel.numConcurrentTest = 0
            configModel.save()

            return configModel

    @staticmethod
    def set_haas_ip(haasip: str):
        configModel = ConfigManager.get_or_create_config()
        configModel.haasIp = haasip
        configModel.save()

    @staticmethod
    def set_haas_port(haasport: int):
        configModel = ConfigManager.get_or_create_config()
        configModel.haasPort = haasport
        configModel.save()

    @staticmethod
    def set_haas_secret(haassecret: str):
        configModel = ConfigManager.get_or_create_config()
        configModel.haasSecret = haassecret
        configModel.save()

    @staticmethod
    def set_num_concurrent_test(concurrenttest: int):
        configModel = ConfigManager.get_or_create_config()
        configModel.numConcurrentTest = concurrenttest
        configModel.save()

    @staticmethod
    def set_haas_configuration(haasip: str, haasport: int, haassecret: str):
        configModel = ConfigManager.get_or_create_config()
        configModel.haasIp = haasip
        configModel.haasPort = haasport
        configModel.haasSecret = haassecret
        configModel.save()