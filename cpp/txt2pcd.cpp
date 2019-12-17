#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include "iostream"
#include  <fstream>
#include <string> 
#include <pcl/surface/convex_hull.h>
#include <pcl/surface/concave_hull.h>
// #include <pcl/filters/statistical_outlier_removal.h>
#include <pcl/filters/radius_outlier_removal.h>

int
  main (int argc, char** argv)
{
  std::ifstream in("/home/lilyxue/Downloads/Cory_room_video_tempt_2_result/sparse/txt0/points3D.txt");
  std::string s;
  int i=0;
  pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);
  cloud->width    = 10000000;
  cloud->height   = 1;
  cloud->is_dense = false;
  cloud->points.resize (cloud->width * cloud->height);
  while (getline(in, s)){
    if (s.find("#")!=std::string::npos) continue;
    // std::cout << s.c_str() << std::endl;

    std::string::size_type pos1, pos2;
    std::vector<std::string> v;
    // std::cout << "hhh" << std::endl;
    pos2 = s.find(" ");
    // std::cout << pos2 << std::endl;
    pos1 = 0;
    while(std::string::npos != pos2)
    {
      v.push_back(s.substr(pos1, pos2-pos1));
    // std::cout << s.substr(pos1, pos2-pos1) << std::endl;
      pos1 = pos2 + 1;
      pos2 = s.find(" ", pos1);
    }
    // if(pos1 != s.length())
    //   v.push_back(s.substr(pos1));
    // std::cout << "ggggggggg" << std::endl;
    // Fill in the cloud data
    // cloud->points[i].z = std::stof(v[1]);
    cloud->points[i].z = 0;
    cloud->points[i].y = std::stof(v[2]);
    cloud->points[i].x = std::stof(v[3]);
    // cloud->points[i].x = 0;
    cloud->points[i].rgb = 256 * 256 * std::stoi(v[4]) + 256 * std::stoi(v[5]) + std::stoi(v[6]);
    ++i;
  }
    cloud->width    = i+1;
    cloud->height   = 1;
    cloud->is_dense = false;
    cloud->points.resize (cloud->width * cloud->height);

      // Create the filtering object
    // pcl::StatisticalOutlierRemoval<pcl::PointXYZRGB> so;
    // so.setInputCloud (cloud);
    // so.setMeanK (50);
    // so.setStddevMulThresh (1.0);
    // so.filter (*cloud);
    pcl::RadiusOutlierRemoval<pcl::PointXYZRGB> outrem;
    // build the filter
    outrem.setInputCloud(cloud);
    outrem.setRadiusSearch(0.05);
    outrem.setMinNeighborsInRadius (2);
    // apply filter
    outrem.filter (*cloud);

        // Create a Concave Hull representation of the projected inliers
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_hull1 (new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::ConvexHull<pcl::PointXYZRGB> chull1;
    chull1.setInputCloud (cloud);
    // chull.setAlpha (0.1);
    chull1.reconstruct (*cloud_hull1);

    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_hull2(new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::ConcaveHull<pcl::PointXYZRGB> chull2;
    chull2.setInputCloud (cloud);
    chull2.setAlpha (0.1);
    chull2.reconstruct (*cloud_hull2);

    pcl::io::savePCDFileASCII ("Cory_room_0_plane.pcd", *cloud);
    pcl::io::savePCDFileASCII ("Cory_room_0_concave_hull.pcd", *cloud_hull2);
    std::cerr << "Saved " << cloud->points.size () << " data points to test_pcd.pcd." << std::endl;

    for (std::size_t i = 0; i < cloud_hull1->points.size (); ++i)
      std::cerr << "    " << cloud_hull1->points[i].x << " " << cloud_hull1->points[i].y << " " << cloud_hull1->points[i].z << std::endl;

  return (0);
}