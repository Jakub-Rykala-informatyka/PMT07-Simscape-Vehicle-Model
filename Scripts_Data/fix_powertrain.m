function fix_powertrain
    % Fixes the sm_car2 powertrain by replacing the broken PMSM variant 
    % with the pristine Mapped Motor variant from sm_car.slx
    
    disp('Loading pristine model sm_car...');
    load_system('sm_car');
    
    disp('Restoring Electric_L1_R1_L2_R2 subsystem...');
    try
        delete_block('sm_car2/Vehicle/Vehicle/Powertrain/Power/Electric_L1_R1_L2_R2');
    catch
        % Might already be deleted or renamed, ignore
    end
    
    add_block('sm_car/Vehicle/Vehicle/Powertrain/Power/Electric_L1_R1_L2_R2', ...
              'sm_car2/Vehicle/Vehicle/Powertrain/Power/Electric_L1_R1_L2_R2');
          
    disp('Saving sm_car2...');
    save_system('sm_car2');
    
    disp('Fix applied successfully! You can now run the simulation.');
end
