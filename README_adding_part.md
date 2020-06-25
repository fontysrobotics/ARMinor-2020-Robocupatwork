README

This readme can be used to create or add a new part ontop of Suii

 <link name="${prefix}name_of_the_part">
      <visual>
        <geometry>
          #filepath to the part you want to import
          <mesh filename="package://path_to_part/name_of_the_part.STL"/>
        </geometry>
        <material name="colour_of_part">
          <color rgba="0.7 0.7 0.7 1.0"/>
        </material>
      </visual>
      <collision>
        <geometry>
          #filepath to the part you want to import
          <mesh filename="package://path_to_part/name_of_the_part.STL"/>
        </geometry>
      </collision>
      <inertial>
      
        #inertial parameters must be containt from solidworks otherwise part will move out of them self
        <mass value= "mass_of_the_part"/>
        <inertia ixx="0" ixy="0" ixz="0" iyy="0" iyz="0" izz="0"/> 
        <origin xyz="0 0 0"  rpy="0 0 0" />
      </inertial>
    </link>

    <joint name="${prefix}joint_name" type="joint_type"> 
      <parent link="${prefix}part_name_from_parent" />
      <child link = "${prefix}part_name_from_child" />

      #sets location and rotation of the part you want to import relative to the parent
      <origin xyz="0 0 0" rpy="0 0 0" />
      <axis xyz="0 1 0" /> 
      
      #sets the limit of the joint
      <limit lower="${-1.6}" upper="${0}" effort="54.0" velocity="3.2"/>
       
      <dynamics damping="0.0" friction="0.0"/>  
    </joint> 