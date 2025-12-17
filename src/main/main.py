import streamlit as st
from knowledge_base import KnowledgeBase
from rule import Rule
from inference_engine import InferenceEngine

def populate_knowledge_base():
    """
    Populates the knowledge base with rules for the tech domain.
    """
    kb = KnowledgeBase()

    rules = [
        # Power Issues
        Rule("R1_CheckPlug", 10, ["computer_wont_turn_on", "power_light_off", "power_cable_unplugged"], "action_plug_in_cable"),
        Rule("R2_CheckPSU", 5, ["computer_wont_turn_on", "power_light_off"], "issue_is_power_supply"), # Lower priority than R1 (Conflict Resolution Demo)
        
        # Display/Boot Issues
        Rule("R3_GPU_Fail", 5, ["screen_black", "fan_running", "beep_codes_heard"], "issue_is_gpu"),
        Rule("R4_Monitor_Off", 5, ["screen_black", "fan_running"], "issue_check_monitor_cable"),
        
        # Internet Issues
        Rule("R5_Wifi_Congestion", 5, ["internet_slow", "wifi_connected", "high_latency"], "issue_wifi_interference"),
        Rule("R6_Ethernet_Check", 5, ["internet_slow", "ethernet_unplugged"], "action_connect_ethernet"),
        
        # OS/Software Issues
        Rule("R7_Driver_Rollback", 8, ["blue_screen_of_death", "new_driver_installed"], "action_rollback_driver"),
        Rule("R8_Disk_Fail", 9, ["system_freeze", "disk_making_noise"], "issue_hard_drive_failure"),
        
        # Maintenance
        Rule("R9_Cleaning", 6, ["overheating", "dusty_vents"], "action_clean_pc"),
        Rule("R10_Thermal_Paste", 4, ["overheating"], "action_replace_thermal_paste"),
        
        # Cascading Logic (Rule implies another fact)
        Rule("R11_Critical_Hardware", 7, ["issue_is_gpu"], "contact_hardware_support"),
        Rule("R12_Critical_Hardware_HDD", 7, ["issue_hard_drive_failure"], "contact_hardware_support"),
        
        # New rules for individual symptom coverage
        Rule("R13_ComputerWontTurnOn", 1, ["computer_wont_turn_on"], "action_check_power_connections"),
        Rule("R14_PowerLightOff", 1, ["power_light_off"], "action_verify_power_source"),
        Rule("R15_PowerCableUnplugged", 1, ["power_cable_unplugged"], "action_plug_in_power_cable"),
        
        Rule("R16_ScreenBlack", 1, ["screen_black"], "action_check_monitor_connection"),
        Rule("R17_FanRunning", 1, ["fan_running"], "action_check_cpu_usage"),
        Rule("R18_BeepCodesHeard", 1, ["beep_codes_heard"], "action_consult_motherboard_manual"),
        
        Rule("R19_InternetSlow", 1, ["internet_slow"], "action_restart_router_modem"),
        Rule("R20_HighLatency", 1, ["high_latency"], "action_check_network_interference"),
        Rule("R21_WifiConnected", 1, ["wifi_connected"], "action_check_internet_service_provider"),
        
        Rule("R22_EthernetUnplugged", 1, ["ethernet_unplugged"], "action_connect_ethernet_cable"),
        Rule("R23_BlueScreenOfDeath", 1, ["blue_screen_of_death"], "action_search_error_code"),
        Rule("R24_NewDriverInstalled", 1, ["new_driver_installed"], "action_check_driver_compatibility"),
        
        Rule("R25_DiskMakingNoise", 1, ["disk_making_noise"], "action_backup_data_check_disk_health"),
        Rule("R26_SystemFreeze", 1, ["system_freeze"], "action_check_event_viewer_for_errors"),
        Rule("R27_DustyVents", 1, ["dusty_vents"], "action_clean_computer_vents")
    ]

    for rule in rules:
        kb.add_rule(rule)

    return kb



def main():

    """

    Main function to run the interactive expert system using Streamlit.

    """

    st.title("Tech Expert System")

    possible_facts = [
        "computer_wont_turn_on", "power_light_off", "power_cable_unplugged", 
        "screen_black", "fan_running", "beep_codes_heard", 
        "internet_slow", "high_latency", "wifi_connected", "ethernet_unplugged",
        "blue_screen_of_death", "new_driver_installed", "disk_making_noise",
        "system_freeze", "dusty_vents", "overheating"
    ]

    selected_symptoms = st.multiselect("Select the symptoms you are experiencing:", options=possible_facts)

    if st.button("Diagnose"):
        kb = populate_knowledge_base()
        engine = InferenceEngine(kb)

        for symptom in selected_symptoms:
            kb.add_fact(symptom)

        initial_facts = kb.get_facts().copy()
        deduced_facts = engine.forward_chain()
        
        solutions = deduced_facts - initial_facts

        st.subheader("Suggested Solutions:")
        if solutions:
            for solution in solutions:
                st.write(f"- {solution.replace('_', ' ').capitalize()}")
        else:
            st.write("No specific solution could be determined from the given symptoms.")

    st.markdown("---") # Separator


if __name__ == "__main__":
    main()
