from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def get_obj_by_name(name, list_of_objs):
        for h in list_of_objs:
            if h.name == name:
                return h

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int,
                          type_software):
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"

        software = type_software(name, capacity_consumption, memory_consumption)

        try:
            hardware.install(software)
            System._software.append(software)

        except Exception as e:
            return 'Software cannot be installed'

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int,
                                  memory_consumption: int):
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, ExpressSoftware)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int,
                                memory_consumption: int):
        return System.register_software(hardware_name, name, capacity_consumption, memory_consumption, LightSoftware)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.get_obj_by_name(hardware_name, System._hardware)
        software = System.get_obj_by_name(software_name, System._software)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum(h.memory for h in System._hardware)
        total_used_memory = sum(h.used_memory for h in System._hardware)
        total_used_space = sum(h.used_space for h in System._hardware)
        total_capacity = sum(h.capacity for h in System._hardware)

        result = f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
                 f"Total Capacity Taken: {total_used_space} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            express_soft = h.get_list_of_obj_by_class_name("expresssoftware")
            light_soft = h.get_list_of_obj_by_class_name("lightsoftware")

            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: {len(express_soft)}\n"
            result += f"Light Software Components: {len(light_soft)}\n"
            result += f"Memory Usage: {h.used_memory} / {h.memory}\n"
            result += f"Capacity Usage: {h.used_space} / {h.capacity}\n"
            result += f"Type: {h.type}\n"
            result += f"Software Components: " \
                      f"{', '.join(s.name for s in h.software_components) if h.software_components else None}"

        return result
